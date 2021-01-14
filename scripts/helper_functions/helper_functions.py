    
def get_headers(fasta_list):
	"""Extracts only headers from list of fasta files."""
	from biofile import get_genome_headers, make_flat
	headers = []
	[headers.append(get_genome_headers(fasta)) for fasta in fasta_list]
	headers = make_flat(headers)
	return headers


def run_process(command, env='', shell=True, capture_output=True, text=True):
	if env:
		print(f'Process runs in : {env}\n')
		"""Runs indicated process and activates indicated environmnet. Ensures environment deactivation"""
		process = subprocess.run(f"""nice -n 5 conda run -n {env} {command}""", capture_output=capture_output, text=text, shell=shell)
	else:
		print(f'Process runs without env.\n')
		process = subprocess.run(f"nice -n 5 conda run {command}", capture_output=capture_output, text=text, shell=shell)
        
	return process

# def message(msg, command='', color=bcolors.OKGREEN):
#     now = datetime.now()
#     print(f'{color}{now:%Y-%m-%d %H:%M} {msg}{bcolors.ENDC}\n')
#     if command: print(f'Command: {command}\n')

def get_jaccard_index(data_sets_single):
	"""List of lists with detections as sets. First element (the first list) is from manually curated prophages."""
	data_sets_jaccard_index = []
	data_sets_TP = []
	# Take list of detections as sets.
	for phage_caller in data_sets_single:    
		phage_caller_list = []
		prophage_caller_TP = []
	    # Interate over true positive prophages.
		for prophage in data_sets_single[0]:
			overlapping = []

			# Iterate over each detection and check if it overlaps with prophage.        
			for detection in phage_caller:
				if prophage.intersection(detection):
					overlapping.append(detection)
					prophage_caller_TP.append(frozenset(detection))

			# Take overlaps and calculate their length.
			n_overlaps = len(overlapping)
			

			# If no overlaps - length of overlaps is 0.
			# Calculate length for one or more overlaps within manually found prophage.
			if n_overlaps == 0: 
				len_overlap = 0
			else:
				many_overlaps = [prophage.intersection(overlap) for overlap in overlapping]
				len_overlaps = [len(overlap) for overlap in many_overlaps]
				len_overlap = sum(len_overlaps)
	        
			len_prophage = len(prophage)
			# Calculate fraction how much of the prophage is being covered by detection(s).
			phage_caller_list.append(len_overlap/len_prophage)

		data_sets_jaccard_index.append(phage_caller_list)
		unique_overlapping_detections = set(prophage_caller_TP)
		data_sets_TP.append(len(unique_overlapping_detections))

	return data_sets_jaccard_index, data_sets_TP




