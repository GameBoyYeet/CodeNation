import os
import random
from time import sleep
from colorama import Fore, Style

tree = """
                                                 
                       +                         
                      ***                        
                     **O**                       
                    *******                      
                   *********                     
                  ***********                   
                   ******o**                     
                  ***********                    
                 ****o********                   
                ***************                  
               ****o***o********                 
              *******************                
            ***********************              
               *****O***********                 
              **********o********                
             ****************o****               
            **O********************              
           ***********o********O****             
         *****************************           
             *********************               
            ***o*******************              
           ***********o*******o*****             
          ***************************            
         ***********************O*****           
        ***O***************************          
      ***********************************        
           *************************             
          *******o********o**********            
         *****************************           
        **************o****************          
       *************************O*******         
      *****O*****************************        
    **************o************************      
          ***************************            
         *************o***************           
        ***********o*******************          
       **************************O******         
      ***o******************O************        
    ***o***********o****************o******      
                      ###                        
                      ###                        
                      ###                        
                      ###                    
                      ###   
"""
lights = ['O', 'o']

colors = list(vars(Fore).values())
tree = tree.replace("*", Fore.GREEN + "*" + Fore.WHITE)
tree = tree.replace("+", Fore.YELLOW + "+" + Fore.WHITE)
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    l = list(tree)

    start = 0
    while start < len(tree):
        replacement = random.choice(colors) + random.choice(lights) + Fore.WHITE
        index = tree.find('O', start)
        if index == -1:
            break
        tree = tree[:index] + replacement + tree[index + len('O'):]
        start = index + len(replacement)

    start = 0
    while start < len(tree):
        replacement = random.choice(colors) + random.choice(lights) + Fore.WHITE
        index = tree.find('o', start)
        if index == -1:
            break
        tree = tree[:index] + replacement + tree[index + len('o'):]
        start = index + len(replacement)

    print("".join(l))
    sleep(1/5)