import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import PurePath
from biofile import parse_file, get_genome_lenght



def complete_vs_contigs(program_complete=[(10,200), (300,500)], program_assembly=[(200,440), (600,900)], contigs=[(10,500),(600,1000)], true_positives=[(10,200), (600,900)],
    is_complete=[(200,300), (800,900)] ,genome_lenght=1000, program='', fname='test-visualise-genome', fpath='/Users/januszkoszucki/', dpi=500):

    from pathlib import Path

    possible_programs =  ['virsorter-complete', 'virsorter-assembly', 'contigs']

    dict_list = []
    plt.figure(num=None, figsize=(10, 1), dpi=dpi)
    plt.title(label=f'{fname}-{program}', fontdict = {'fontsize': 7}, loc='center', y=1.05)

    genome_line = [(0, genome_lenght)]
    heights = [5, 11, 11, 11, 15, 22]
    width = [10, 2, 2, 2, 6, 10]
    hues = list(sns.color_palette('pastel')[2:7])
    hues.insert(2, list(sns.color_palette('dark')[2]))
    hues.insert(3, list(sns.color_palette('dark')[3]))

    for hlines, height, lw, hue in zip([program_complete, genome_line, true_positives, is_complete,contigs, program_assembly], heights, width, hues):
        for line in hlines:
            start = line[0]
            end = line[1]
            plt.hlines([height], start, end, lw=lw, colors=hue)

    plt.ylim(0, sum(heights)-27)
    plt.xlim(0, genome_lenght)
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.savefig(str(Path(fpath, fname + '-' + program +'.png')), bbox_inches='tight', dpi=dpi)
    plt.show()



def visualise_genome(genome_path, genome_lenght, dpi=500):
    possible_confidences = ['Not-determined', 'Low-quality', 'Medium-quality', 'High-quality', 'Complete']
    possible_programs =  ['virsorter', 'phispy', 'allcontigs', 'contigs', 'virsorter-assembly', 'provirus', 'manual']
    # palettes_program = ['mako', 'mako', 'rocket', 'viridis', 'pastel']

    dict_list = []
    plt.figure(num=None, figsize=(6, 4), dpi=dpi)
    plt.title(label=genome_path.stem, fontdict = {'fontsize': 10}, loc='center', y=0.5)

    for program in possible_programs:
        program_path = PurePath(genome_path, 'coordinates_' + program)
        try:
            columns = parse_file(program_path)
        except OSError as error:
            continue

        if columns:
            starts = columns[0]
            ends = columns[1]
            confidence = columns[2]
            program = columns[3][0]
            if program == 'assembly': program = 'virsorter-assembly'
        else:
            continue

        for i, possible_program in enumerate(possible_programs):
            if program == possible_program:
                height = i/3 + 0.2
            else:
                continue

        if program == 'virsorter' or program == 'phispy':
            palette = 'mako'
            hues = []
            for dectection_conf in confidence:
                for hue, conf in enumerate(possible_confidences):
                    if dectection_conf == conf:
                        hues.append(sns.color_palette(palette)[hue])

        else:
            hues = []
            for detection_conf in confidence:
                if program == 'virsorter-assembly':
                    program_hue = 1
                    hues.append(sns.color_palette()[program_hue])
                elif program == 'provirus':
                    program_hue = 2
                    hues.append(sns.color_palette()[program_hue])
                elif program == 'manual':
                    program_hue = 4
                    hues.append(sns.color_palette()[program_hue])
                elif program == 'contigs':
                    program_hue = 5
                    hues.append(sns.color_palette()[program_hue])
                elif program == 'allcontigs':
                    program_hue = 5
                    hues.append(sns.color_palette()[program_hue])
                # else:
                #     hues.append(sns.color_palette()[-1])

        my_dict = {'program': program,
                  'height': height,
                  'coordinates':{
                      'starts': starts,    # Start sorter by confidence
                      'ends': ends,
                      'hues': hues,        # List of colors from color_pallette corresponding to confidence.
                  }}

        dict_list.append(my_dict)

    for d in dict_list:
        height = d['height']
        starts = d['coordinates']['starts']
        ends = d['coordinates']['ends']
        hues = d['coordinates']['hues']

        for start, end, hue in zip(starts, ends, hues):

            plt.hlines([round(height+0.2, 2)], int(start), int(end), lw=10, colors=hue)

        plt.ylim(0, 1 * len(dict_list))
        plt.xlim(0, genome_lenght)
        plt.gcf().subplots_adjust(top=0.16 * len(dict_list))
        plt.gca().axes.get_yaxis().set_visible(False)
        plt.savefig(fname=f'/Users/januszkoszucki/Desktop/{genome_path.stem}.png', bbox_inches='tight', dpi=dpi)
    print(genome_path.stem)
    plt.show()
