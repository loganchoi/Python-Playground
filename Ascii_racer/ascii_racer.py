def hitWall(tracks,curr_row):
    if '|^' in tracks[curr_row]:
        print("\033[H\033[J")
        print(''' 
     _.--"""""--._                                                                                                                    
   .'             '.                                                                                                                  
  /                 \                                                                                                                 
 ;                   ;                                                                                                                
 |                   |                                                                                                                
 |                   |                                                                                                                
 ;                   ;                                                                                                                
  \ (`'--,    ,--'`) /                                                                                                                
   \ \  _ )  ( _  / /                                                                                                                 
    ) )(')/  \(')( (                                                                                                                  
   (_ `""` /\ `""` _)                                                                                                                 
    \`"-, /  \ ,-"`/                                                                                                                  
     `\ / `""` \ /`                                                                                                                   
      |/\/\/\/\/\|                                                                                                                    
      |\        /|                                                                                                                    
      ; |/\/\/\| ;                                                                                                                    
       \`-`--`-`/                                                                                                                     
        \      /                                                                                                                      
         ',__,'                                                                                                                       
          q__p                                                                                                                        
          q__p                                                                                                                        
          q__p                                                                                                                        
          q__p

You hit the wall and lose! ''')
	return False
    elif '^|' in tracks[curr_row]:
        print("\033[H\033[J")
        print('''
      .--"""""--._
   .'             '.
  /                 \
 ;                   ;
 |                   |
 |                   |
 ;                   ;
  \ (`'--,    ,--'`) /
   \ \  _ )  ( _  / /
    ) )(')/  \(')( (
   (_ `""` /\ `""` _)
    \`"-, /  \ ,-"`/
     `\ / `""` \ /`
      |/\/\/\/\/\|
      |\        /|
      ; |/\/\/\| ;
       \`-`--`-`/
        \      /
         ',__,'
          q__p
          q__p
          q__p
          q__p

You hit the wall and lose!''')
	return False
    else:
	return True


def ValidInput(letter):
    theList = ['y','n']
    while letter not in theList:
        letter = input('Do you want to play again (y | n)?')
    
    return letter
    

def ascii_racer():
	 my_lib = [' |*  ^  *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              '|*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              ' |*     *|',
              '|*     *|',
              ' |*     *|',]

    play = True
    while play == True:
        print("\033[H\033[J")
        print('''

                              _.-="_-
                         _.-="   _-          | ||"""""""---._______     __..
             ___.===""""-.______-,,,,,,,,,,,,`-''----" """""       """""  __'
      __.--""     __        ,'                   o \           __        [__|
 __-""=======.--""  ""--.=================================.--""  ""--.=======:
]       [w] : /        \ : |========================|    : /        \ :  [w] :
V___________:|          |: |========================|    :|          |:   _-"
 V__________: \        / :_|=======================/_____: \        / :__-"
 -----------'  "-____-"  `-------------------------------'  "-____-"

Welcome to ASCII-racer,
Navigate through to the light at the end of the tunnel to win!
Press 'a' for left, 'd' for right', enter for nothing.
If you hit the walls, youlose.
To win, you have to complete 2 laps around the tunnel array.
Press any key to start! ''')
	anyKey = input()
        print("\033[H\033[J")
        row = 0
        lap =1
        index = -4
        while row < 19:
            print('ASCII racer 1.0: level:',row,'of 23 rows in lap number', lap)
            print('''

    _------_                                                                                                                          
  -~        ~-                                                                                                                        
 -     _      -                                                                                                                       
-      |>      -                                                                                                                      
-      |<      -                                                                                                                      
 -     |>     -                                                                                                                       
  -    ||    -                                                                                                                        
   -   ||   -                                                                                                                         
    -__||__-                                                                                                                          
    |______|                                                                                                                          
    <______>                                                                                                                          
    <______>                                                                                                                          
       \/
		''')
	    print(my_lib[row+2])
            print(my_lib[row + 1])
            print(my_lib[row])
            move = input()
            if move == 'a':
                index = - 4
                tempstr = my_lib[row+1]
                tempstr = tempstr[:(index+1)]+'^'+tempstr[(index+1):]
                my_lib[row+1] = tempstr
                index = index+1
                Wall = hitWall(my_lib,row)
                if Wall == False:
                    break
            elif move == 'd':
                index = -4
                tempstr = my_lib[row+1]
                tempstr= tempstr[:(index-1)] + '^' + tempstr[(index+1):]
                my_lib[row+1] = tempstr
                index = index - 1
                Wall = hitWall(my_lib,row)
                if Wall == False:
                    break
	    else:
                tempstr = my_lib[row+1]
                tempstr = tempstr[:index]+'^'+tempstr[index:]
                my_lib[row+1] = tempstr
                index = index
                Wall = hitWall(my_lib,row)
                if Wall == False:
                    break
	    print("\033[H\033[J")
            row = row + 1
	if Wall == True:
	    lap = 2
	    row = 0
	    while row<24:
		print('ASCII racer 1.0: level:',row-19,'of 23 rows in lap number', lap)
		print ('''

    _------_                                                                                                                          
  -~        ~-                                                                                                                        
 -     _      -                                                                                                                       
-      |>      -                                                                                                                      
-      |<      -                                                                                                                      
 -     |>     -                                                                                                                       
  -    ||    -                                                                                                                        
   -   ||   -                                                                                                                         
    -__||__-                                                                                                                          
    |______|                                                                                                                          
    <______>                                                                                                                          
    <______>                                                                                                                          
       \/ 

''')
		print(my_lib[row+2])
                print(my_lib[row + 1])
                print(my_lib[row])
                move = input()
                if move == 'a':
                    index = - 4
                    tempstr = my_lib[row+1]
                    tempstr = tempstr[:(index+1)]+'^'+tempstr[(index+1):]
                    my_lib[row+1] = tempstr
                    index = index+1
                    Wall = hitWall(my_lib,row)
                    if Wall == False:
                        break
                elif move == 'd':
                    index = -4
                    tempstr = my_lib[row+1]
                    tempstr= tempstr[:(index-1)] + '^' + tempstr[(index+1):]
                    my_lib[row+1] = tempstr
                    index = index - 1
                    Wall = hitWall(my_lib,row)
                    if Wall == False:
                        break
                
                else:
                    tempstr = my_lib[row+1]
                    tempstr = tempstr[:index]+'^'+tempstr[index:]
                    my_lib[row+1] = tempstr
                    index = index
                    Wall = hitWall(my_lib,row)
                    if Wall == False:
                        break
                row = row + 1
                print("\033[H\033[J")
	  
	if Wall == True:
	    print('''
                         .''.                                                                                               
       .''.      .        *''*    :_\/_:     .                                                                                        
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.                                                                                     
  .''.: /\ :    /)\   ':'* /\ *  : '..'.  -=:o:=-                                                                                     
 :_\/_:'.:::.  | ' *''*    * '.\'/.'_\(/_ '.':'.'                                                                                     
 : /\ : :::::  =  *_\/_*     -= o =- /)\     '                                                                                        
  '..'  ':::' === * /\ *     .'/.\'.  ' ._____                                                                                        
      *        |   *..*         :       |.   |' .---"|                                                                                
        *      |     _           .--'|  ||   | _|    |                                                                                
        *      |  .-'|       __  |   |  |    ||      |                                                                                
     .-----.   |  |' |  ||  |  | |   |  |    ||      |                                                                                
 ___'       ' /"\ |  '-."".    '-'   '-.'    '`      |____                                                                            
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                                                                            
                       ~-~-~-~-~-~-~-~-~-~   /|                                                                                       
                 ~-~-~-~-~-~-~-~  /|~       /_|\                                                                                      
        ~-~-~-  -~-~-~-~-~-~     /_|\    -~======-~                                                                                   
~-~~~~~~~~~~~~~     ~-~-~-~     /__|_\ ~-~-~-~                                                                                        
~-~-~-~-~-~    ~-~~-~-~-~-~    ========  ~-~-~-~                                                                                      
      ~-~~-~-~-~-~-~-~-~-~-~-~-~ ~-~~-~-~-~-~                                                                                         
                        ~-~~-~-~-~-~              

You win!
''')

        playAgain = input('Do you want to play again (y | n)?')
        playAgain = ValidInput(playAgain)
        if playAgain == 'n':
            break
        else:
            continue 

if __name__ == '__main__':
    ascii_racer()
