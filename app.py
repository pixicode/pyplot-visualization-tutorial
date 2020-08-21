import matplotlib.pyplot as plt
import json


def generate_random_data():
    pass


def main():

    with open("input.json", "r") as f:
        posts_arr = json.load(f)

    print(posts_arr)
    data_point_map = {
        "python": [], 
        "node": [], 
        "react": [],
        "ios": []
    }

    for input_data in posts_arr:
        for k in data_point_map:
            if k in input_data:
                data_point_map[k].append(input_data[k])
            else:
                data_point_map[k].append(0)
    
    print(data_point_map)

    for key, arr in data_point_map.items():
        plt.plot(range(len(arr)), arr, marker="o", label=key)

    plt.ylabel("Job Posts")
    plt.title("Simple Plot")
    plt.legend()
    plt.savefig("output.png")
    plt.clf()

    sum_of_data = [sum(x) for x in data_point_map.values()]
    plt.pie(sum_of_data, labels=data_point_map.keys())
    my_circle = plt.Circle( (0,0), 0.7, color='white')
    plt.gcf().gca().add_artist(my_circle)

    plt.savefig("pie_output.png")

if __name__ == "__main__":
    main()