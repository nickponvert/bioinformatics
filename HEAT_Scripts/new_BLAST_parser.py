from Bio.Blast import NCBIXML
result_handle=open('/home/nick/Desktop/QueryA_out.xml')
records_1=NCBIXML.parse(result_handle)
hit_names=[]

for record in records_1:
    for alignment in record.alignments:
        align_name_split=str(alignment.title).split(' ')
        hit_names.append(align_name_split[1])
        #print align_name_split[1]