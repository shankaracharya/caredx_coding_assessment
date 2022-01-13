from argparse import ArgumentParser

def calculate_maf(referenceAC, alternateAC):
    maf = float(min(referenceAC, alternateAC)/(referenceAC + alternateAC))
    return maf


def main(input_file, output_file):
    count=0
    with open (input_file, "r") as input:
        lines = input.readlines()[1:]
    with open(output_file, "w") as output:
        output.write("SNPname\tMAF\n")
        for line in lines:
            tab_split = line.strip().split("\t")
            maf = calculate_maf(int(tab_split[1]), int(tab_split[2]))
            output.write(tab_split[0] + "\t" + str("%.3f" % round(maf, 3)) + "\n")
            if 0.020 <= round(maf, 3) <= 0.3:
                count = count + 1
    print(output_file + "\t" + str(count))

if __name__ == "__main__":
    parser = ArgumentParser(description="coding assessment")
    parser.add_argument(
        "--input",
        dest="input",
        help="input_file",
        type=str,
        required=True
    )
    parser.add_argument(
        "--output",
        dest="output",
        help="output_file",
        type=str,
        required=True
    )

    args = parser.parse_args()
    main(
        args.input,
        args.output
    )
