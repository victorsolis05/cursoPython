from functools import reduce
import operator
from colorama import Fore
from colorama import Style


def generarReporte(candidates:dict):
    total =  reduce(lambda x,y: x + y, candidates.values(), 0)
    #winer = max(candidates.items(), key=operator.itemgetter(1))
    winer = max(candidates, key=candidates.get)
    candidates = "\n".join(list(map(lambda x:  f"{x[0]} : {round((x[1]* 100) / total,1)}  % ({x[1]})" , candidates.items())))
    return f'''
{Fore.BLUE}Election Results
{Fore.YELLOW}====================================
{Fore.GREEN}Total votes: {total}
{Fore.YELLOW}====================================
{Fore.CYAN}{candidates}
{Fore.YELLOW}====================================
{Fore.RED}Winer: {winer}
{Style.RESET_ALL}
'''