from Bio import SeqIO


def parse_file(path):
    """Reads file and appends each columns as a list to a list.
    Output: list of lists - list of columns."""
    columns = []
    with open(path, 'r+') as f:
        rows = [line.strip().split() for line in f.readlines()]

    if rows:
        for cell, element in enumerate(rows[0]):
            column = [row[cell] for row in rows]
            columns.append(column)
    else: columns = []
    return columns


def load_file(path):
    """Takes as an input a path to a file with filenames. Loads them to a list."""
    with open(path ,'r') as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


def save_lines(lines, path):
    """Saves lines to file. If lines are empty creates empty file."""
    if lines:
        with open(path, 'w+') as f:
            [f.write(line) for line in lines]
    else:
        with open(path, 'w+') as f:
            f.write('')

def prepare_to_save(line):
    if line:
        strs = [str(x) for x in line]
        line = '   '.join(strs)
        line = f'{line}\n'
    else:
        line = ''
    return line


def make_flat(my_list):
    flat_list = [item for sublist in my_list for item in sublist]
    return flat_list


def get_genome_lenght(genome_path, ftype='fasta'):
    """Does it work properly?"""
    from Bio import SeqIO
    """Get lenght of the analyzed genome."""
    seq_record = SeqIO.parse(genome_path, ftype)
    sequence = next(seq_record).seq
    return len(sequence)


def get_genome_length(genome_path, ftype='fasta'):
    """Does it work properly?"""
    from Bio import SeqIO
    """Get lenght of the analyzed genome."""
    seq_record = SeqIO.parse(genome_path, ftype)
    sequence = next(seq_record).seq
    return len(sequence)

# def get_genomes(iterate_files_path):
#     """Load names of genomes from iterate_files.txt"""
#     with open(iterate_files_path, 'r+') as f:
#         genomes = [line.strip() for line in f.readlines()]
#     return genomes


def get_genome_headers(path, ftype='fasta'):
    from Bio import SeqIO
    """Get header of the genome."""
    headers = [seq.id for seq in SeqIO.parse(path, ftype)]
    return headers

def save_coordinates():
    print("need to be written")
    pass


def extract_chromosome():
    pass
