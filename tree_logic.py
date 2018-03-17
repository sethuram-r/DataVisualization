
import csv
import json

INPUT_CSV = "/Users/sethuram/Desktop/test/output.csv"
OUT_JSON = "/Users/sethuram/Desktop/test/output.json"

from copy import deepcopy

# keeps track of the
child_industries_record = {}
leaf = {"name": "", "children": []}


def initialise(a):
    new_indus_leaf = deepcopy(leaf)
    new_indus_leaf_two = deepcopy(leaf)
    new_indus_leaf_three = deepcopy(leaf)
    new_indus_leaf_three["name"] = "Total no of jobs: " + a["numberofpositions"]
    new_indus_leaf_three["children"] = []
    new_indus_leaf_two["name"] = a["skills"]
    new_indus_leaf_two["children"] = [new_indus_leaf_three]
    new_indus_leaf["name"] = a["industry"]
    industry.append([loc, a["industry"], a["skills"]])
    new_indus_leaf["children"] = [new_indus_leaf_two]
    return new_indus_leaf




with open(INPUT_CSV) as csvfile:
    a = csv.DictReader(csvfile)
    locations = []
    value = []
    skills = list(set())
    industry = list()
    for row in a:
        locations.append(row['joblocation_address'])

        value.append(row)
        locations = list(set(locations))
        locations = list(filter(None, locations))  # to remove empty strings

        data = {"name": "JOBS", "children": []}

    for loc in locations:
        data["children"].append({"name": loc, "children": []})

        for a in value:
            if (a["joblocation_address"] == loc):

                for indus in data["children"]:  # top level with locations
                    if (indus["name"] == loc):
                        key = loc + "." + a["industry"]  # key to the dict which keeps track of the index of industries
                        if indus["children"] == []:  # at the start when there are no industry
                            child_industries_record[key] = 0
                            indus["children"].append(initialise(a))
                        elif key not in child_industries_record:  # this particular index in
                            child_industries_record[key] = len(indus["children"])
                            indus["children"].append(initialise(a))
                        else:
                            for ind in industry:
                                if(ind[0]== loc and ind[1]== a["industry"] and ind[2] ==  a["skills"] ):
                                    index = child_industries_record[key]
                                    new_count = int(indus["children"][index]["children"][0]["children"][0]["name"].split(": ")[1])  + int(a["numberofpositions"])
                                    indus["children"][index]["children"][0]["children"][0]["name"] = "Total no of jobs: " + str(new_count)




    with open(OUT_JSON, "w") as output_f:
        json.dump(data, output_f)

print(json.dumps(data, indent=4))