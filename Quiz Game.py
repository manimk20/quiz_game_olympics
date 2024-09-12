def run_quiz(questions):
    score = 0
    for question in questions:
        print(question['prompt'])
        for option in question['options']:
            print(option)
        answer = input('Enter your answer (A, B, C, D): ').upper()

        if answer == question['answer']:
            print('Correct, Hooray!!!\n')
            score += 1
        else:
            print(f'Wrong, Looser!! The correct answer is {question["answer"]}.\n')
    print(f'You got {score} out of {len(questions)} questions correct.')

questions = [
    {
        'prompt': 'In which year did the first modern Olympic Games take place?',
        'options': ['A. 1896', 'B. 1900', 'C. 1924', 'D. 1888'],
        'answer': 'A'
    },
    {
        'prompt': 'Which city hosted the Summer Olympics in 2008?',
        'options': ['A. Athens','B. Beijing','C. London','D. Rio de Janeiro'],
        'answer': 'B'
    },
    {
        'prompt': 'Which country has won the most medals in the history of the Winter Olympics?',
        'options': ['A. Canada', 'B. Norway', 'C. Germany','D. United States'],
        'answer': 'B'
    },

    {
        'prompt': 'Who is the most decorated Olympian of all time?',
        'options': ['A. Usain Bolt', 'B. Michael Phelps','C. Carl Lewis','D. Larisa Latynina'],
        'answer': 'B'
    },

    {
        'prompt': 'Which city has hosted the Summer Olympics the most times?',
        'options': ['A. London', 'B. Paris', 'C. Los Angeles', 'D. Tokyo'],
        'answer': 'A'
    },

    {
        'prompt': 'Which Olympic sport combines cross-country skiing and rifle shooting?',
        'options': ['A. Pentathlon','B. Biathlon','C. Triathlon','D. Decathlon'],
        'answer': 'B'
    },

    {
        'prompt': 'In which year were the first Winter Olympics held?',
        'options': ['A. 1920','B. 1924','C. 1936','D.1948'],
        'answer': 'B'
    },

    {
        'prompt': 'What do the five interlocking rings of the Olympic flag represent?',
        'options': ['A. The five continents of the world','B. The five founding nations of the Olympics','C. The five core sports','D. The first five host cities'],
        'answer': 'A'
    },

    {
        'prompt': 'Which country has won the most gold medals in Summer Olympic history?',
        'options': ['A. China','B. Germany','C. Russia','D. United States'],
        'answer': 'D'
    },

    {
        'prompt': 'Which of the following sports was introduced to the Summer Olympics in 2020?',
        'options': ['A. Surfing','B. Rugby','C. Golf','D. Badminton'],
        'answer': 'A'
    }
]
run_quiz(questions)



