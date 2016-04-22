"""

USed for adapter removal benchmarks. 

May not be used on long term. 

May be removed

"""



def fasta_fwd_rev_to_columns(file1, file2=None, output_filename=None):
    """Reads FWD and (optional) REV adapters in FASTA and save
    into a column-style file


    """

    import pysam
    f1 = pysam.FastxFile(file1)
    if output_filename is not None:
        fout = open(output_filename, "w")
    if file2:
        f2 = pysam.FastxFile(file2)
        for read1, read2 in zip(f1, f2):
            txt = "%s %s" % (read1.sequence, read2.sequence)
            if output_filename is None:
                print(txt)
            else:
                fout.write(txt+"\n")
    else:
        for read1 in f1:
            txt = "%s" % read1.sequence
            if output_filename is None:
                print(read1.sequence, read2.sequence)
            else:
                fout.write(txt+"\n")
    if output_filename is not None:
        fout.close()


def adapters_files_to_list(filename1, filename2):

    fh1 = open(filename1, 'r')
    fh2 = open(filename1, 'r')
    data1 = fh1.readlines()
    data2 = fh2.readlines()
    fh1.close()
    fh2.close()

    len(data1) == len(data2), "incompatible files. Must have same length"

    fh = open("adapters_list.fa", 'w')
    count = 0
    for line1, line2 in zip(data1, data2):
        line1 = line1.strip()
        line2 = line2.strip()
        if line1.startswith(">"):
            pass
        else:
            fh.write(line1+" " +line2+ "\n")
            count += 1

    fh.close()
    print("Saved %s adapters in adapters_combined.fa" % count)


def adapters_to_clean_ngs(filename):
    fh1 = open(filename, 'r')
    data1 = fh1.readlines()
    fh1.close()

    count = 0
    fh = open("adapters_ngs.txt", "w")
    for line in data1:
        line = line.strip().strip("\n")
        if line.startswith('>'):
            pass
        else:
            data = "adapter_%s\t%s\t0.5\t31\t10\t0\t0\n"% (count+1, line)
            fh.write(data)
            count+=1
    fh.close()



#adapters_to_clean_ngs("adapters_48_PCR-free_FWD.fa")
#if __name__ == "__main__":
#    import sys
#    args = sys.argv
#    adapters_files_to_list(args[1], args[2])


def adapter_removal_parser(filename):
    """Parses output of AdapterRemoval"""
    results = {}

    with open(filename, "r") as fin:
        lines = fin.readlines()
        for line in lines:
            if line.startswith("  --adapter"):
                lhs, rhs = line.split(":")
                name = lhs.strip().replace("-", "")
                sequence = rhs.strip()
                results[name] = sequence
    return results









