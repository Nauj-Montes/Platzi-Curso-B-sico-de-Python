def main():
    my_dictionary = {
        "key1": 1,
        "key2": 2,
        "key3": 3
    }
    # print(my_dictionary)

    # print(my_dictionary["key1"])
    # print(my_dictionary["key2"])
    # print(my_dictionary["key3"])

    population = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424
    }

    # for countries in population.keys():
    #     print(countries)

    # for people in population.values():
    #     print(people)

    for country, people in population.items():
        print(country + " have about " + str(people) + " population.")


if __name__ == "__main__":
    main()
