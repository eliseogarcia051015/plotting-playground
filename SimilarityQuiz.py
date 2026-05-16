import numpy as np

def similarity(v1, v2):
    dist = np.linalg.norm(v1 - v2)
    max_dist = np.sqrt(len(v1) * (5 - 1)**2)
    return 1 - (dist / max_dist)


def main():
    print("This is a simple test")
    questions = {   
        "0": "Do you like pizza (1-5): ",
        "1": "Do you like dogs (1-5): ",
        "2": "Do you like the outdoors (1-5): ",
        "3": "Do you like sports (1-5): ",
    }
    responses = []
    users = 2
    for i in range(users):
        print(f"\nUser {i+1} Quiz")
        user_answer = []
        for q in questions:
            answer = int(input(questions[f"{q}"]))
            user_answer.append(answer)
        responses.append(np.array(user_answer))
    print(responses)
    print(f"\nSimilarity: {similarity(responses[0],responses[1])*100:.2f}%")


if __name__ == "__main__":
    main()