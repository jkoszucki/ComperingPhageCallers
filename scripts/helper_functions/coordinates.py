
def get_phispy_coordinates(prophage_table_tsv_path):
	coordinates = []
	try:
		with open(next(prophage_table_tsv_path), 'r') as f:
			phages_list = [line.strip().split()[1:4] for line in f.readlines()]
	except:
		return [(0,0)], [0]

	try:
		[coordinates.append((int(phage[1]), int(phage[2]))) for phage in phages_list]
	except:
		coordinates.append((0,0))


	contig_ids = []
	for phage in phages_list:
		conitg_id = phage[0]
		try:
			contig_ids.append(int(conitg_id))
		except:
			pass

	return coordinates, contig_ids


def get_virsorter_coordinates(fasta_paths_list):
	"""Extracts coordinates from list of headers from fasta file.
	Returns list of coordinates (if whole contig was detected 0,0 tuple is appended as a place holder).
	contig_id list return list of contigs id's if file had them, otherwise list of genome names.
	"""
	import helper_functions as hf
	headers_list = hf.get_headers(fasta_paths_list)

	coordinates = []
	for header in headers_list:
		if len(header.split('-')) > 2:
			coordinates.append((int(header.split('-')[-3]), int(header.split('-')[-2])))
		else:
			coordinates.append((0,0))

	contig_ids = []
	for header in headers_list:
		contig_id = header.split('_')[1]
		try:
			contig_ids.append(int(contig_id))
		except: break

	return coordinates, contig_ids


def get_absolute_coordinates(program_contigs=[((10,100),1), ((200,300),2)], contigs=[((600,800), 'forward', 1), ((100,300), 'forward', 2)]):
	"""Maps detected prophages to contigs and re-calculates their position on complete genome.
	List of tuples with tuple as start and end propahges or contigs with int as contig ids."""
	for program_contig in program_contigs:
		for contig in contigs:
			if program_contig[-1] == contig[-1]:
				index = program_contigs.index(program_contig)
				matched_contig = program_contigs.pop(index)
				(start, end), matched_id = matched_contig
				contig_start, contig_end = contig[0]

				if program_contig[0] == (0,0):
					program_contigs.insert(index, ((contig_start, contig_end), matched_id))
				else:
					if contig[-2] == 'revers':
						phage_len = end - start
						new_start = contig_start + (contig_end - (contig_start + end))
						program_contigs.insert(index, ((new_start, new_start + phage_len), matched_id))
					else:
						program_contigs.insert(index, ((contig_start + start, contig_start + end), matched_id))
	return program_contigs


def parse_abacas_contigs(contigs):
	coordinates = []
	orientation = []
	ids = []
	for contig in contigs:
		if 'contig' in contig:
			if 'complement' in contig:
				coordinates.append((int(contig[21:].strip('complement()').split('..')[0]),
				int(contig[21:].strip('complement()').split('..')[1])))
				orientation.append('revers')
			else:
				coordinates.append((int(contig[21:].split('..')[0]),
				int(contig[21:].split('..')[1])))
				orientation.append('forward')

		elif 'systematic_id' in contig:
			ids.append(int(contig.split("\"")[-2]))
	return list(zip(coordinates, orientation, ids))
