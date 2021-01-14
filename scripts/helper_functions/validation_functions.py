class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def create_folders(*args):    
    """Create folders. Accepts Path objects."""
    [folder.mkdir(parents=True, exist_ok=True) for folder in args]
    
def run_process(command, env='', shell=True, capture_output=True, text=True):
    if env:
        print(f'Process runs in : {env}\n')
        """Runs indicated process and activates indicated environmnet. Ensures environment deactivation"""
        process = subprocess.run(f"""nice -n 5 conda run -n {env} {command}""", capture_output=capture_output, text=text, shell=shell)
    else:
        print(f'Process runs without env.\n')
        process = subprocess.run(f"nice -n 5 conda run {command}", capture_output=capture_output, text=text, shell=shell)
        
    return process

def message(msg, command='', color=bcolors.OKGREEN):
    now = datetime.now()
    print(f'{color}{now:%Y-%m-%d %H:%M} {msg}{bcolors.ENDC}\n')
    if command: print(f'Command: {command}\n')
        

def fix_header(infile):
    """Fixes the locus header of the genbank file annotated by prokka. Necessary to lunch phispy."""
    with open(infile, 'r') as f:
        lines = [line for line in f.readlines()]
    header = lines.pop(0)
    new_header = ' '.join(header.split('_'))
    lines.insert(0, new_header)
    save_lines(lines, infile)

    
def coordinates_to_positions(positions_set):
    """e.g. input: {(975111, 976555), (1459781, 1461225), (2076590, 2078034)}"""
    positions_set = [tuple(IS) for IS in positions_set]
    positions_set = [set((np.arange(IS[0], IS[1]))) for IS in positions_set]
    return positions_set


def get_IS_overlaps(positions_list):
    """list_of_sets with posistions: e.g. [{1,2,3,4}, {10,12,13,14}, {4,5,6,7,8}]. Use np.arange function."""
    alloverlaps = []
    for IS1 in positions_list:
        overlap = []
        for IS2 in positions_list:
            overlap.append(len(IS1.intersection(IS2))/len(IS1))
        alloverlaps.append(overlap)
    return alloverlaps


def get_indicies_to_drop(overlaps):
    indcies_to_drop = []
    for index, IS_overlaps in enumerate(overlaps):
        for i, IS_pair_overlap in enumerate(IS_overlaps[index:]):
            if IS_pair_overlap > 0.5 and IS_pair_overlap != 1.0:
                indcies_to_drop.append(index + i)
                
    indcies_to_drop = list(set(indcies_to_drop))
    return indcies_to_drop

def drop_indicies(indicies_to_drop, is_complete_positions):
    for i in sorted(indicies_to_drop, reverse=True):
        del is_complete_positions[i]
    return is_complete_positions