import csv


def read_data_csv(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        data = list(csv.reader(file))

    data = [dict(zip(data[0], row)) for row in data[1:]]

    splited_data = []

    for i in range(len(data)):
        splited_data.append(data[i])

    return splited_data


def generate_response(user_input, data):
    response = "There is no data here for the search term."
    user_input = user_input.lower()

    for country in data:
        if "Country" in country:
            country_name = country["Country"].strip().lower()
            if user_input == country_name:
                return country

    return response


def main():
    data = read_data_csv("countries_of_the_world.csv")

    for d in data:
        country_name = d["Country"]
        print(country_name.strip())

    while True:
        user_input = input("Enter a search term: ")
        if user_input.lower() == "exit":
            break

        response = generate_response(user_input, data)
        print(response)


if __name__ == "__main__":
    main()
