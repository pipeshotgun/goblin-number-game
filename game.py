print('welcome to my Game')

choice = input('type start to begin ')


if  choice == "start":
    print('Starting game...')

else:
    print('Invalid choice. Please type "start" to begin.')
    quit()

if choice == "start":
    print('you start in a forest two paths before , chose one of them: Path 1 or Path 2')
    choice = input('which path do you choose? ')

if choice =='path 1' or choice == ' 1':
  print('You choose Path 1.')
  print('you follow down the path and see a gooblin in the distance.')


if choice == 'path 2':
  print('You have been killed by a swarm of bees.')
  print('You died.')
  quit()    

choice = input('Do you want to approach the goblin or run away? (approach/run) ')

if choice == 'approach':
    print('You approach the goblin.')
    choice = input('the goblin says if you wish you pass you must asnwer these questions: What is 2+2? ')

    if choice == '4':
        print('Correct! You may pass.')
    else:
        print('Incorrect. You are not allowed to pass.')
        print('You died.')


if choice == 'run':
    print('thw goblin kiled you.' \
    ' You died.')


if choice == '4':
    print('Good job since you think your so smart what is 2 * 2 ?')
    choice = input('What is 2 * 2 ? ')

    if choice == '4':
        print('Correct! You may pass.')
    else:
        print('Incorrect. You are not allowed to pass.')
        print('You died.')


if choice == '4':
    print('You have successfully passed the goblin\'s test.')
print('you have completed the game.')
