import numpy as np

def similarity(v1, v2):
    dist = np.linalg.norm(v1 - v2)
    max_dist = np.sqrt(len(v1) * (5 - 1)**2)
    return 1 - (dist / max_dist)


def main():
    print("This is a simple test")
    responses = []
    users = 2
    for i in range(users):
        print(f"\nUser {i+1} Quiz")
        question1 = int(input("Do you like pizza (1-5): "))
        question2 = int(input("Do you like dogs (1-5): "))
        question3 = int(input("Do you like the outdoors (1-5): "))
        question4 = int(input("Do you like sports (1-5): "))
        response = np.array([question1, question2, question3, question4])
        responses.append(response)
    print(responses)
    print(f"\nSimilarity: {similarity(responses[0],responses[1])*100:.2f}%")


if __name__ == "__main__":
    main()