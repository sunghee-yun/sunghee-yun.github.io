"""
create html escape character tables
"""

from click import command, argument, Path
import os


@command()
@argument("output_dir", type=Path(exists=True, file_okay=False, dir_okay=True, readable=True))
def main(output_dir: str) -> None:

    with open(os.path.join(output_dir, "styles.css"), "w") as fid:

        def write(string: str) -> None:
            fid.write(f"{string}\n")

        write("table {")
        write("\tborder-collapse: collapse;")
        write("\twidth: 100%;")
        write("\tmax-width: 800px;")
        write("\tmargin: 20px auto;")
        write("}")
        write("th, td {")
        write("\tborder: 1px solid #ddd;")
        write("\tpadding: 8px;")
        write("\ttext-align: center;")
        write("}")
        write("th {")
        write("\tbackground-color: #f2f2f2;")
        write("\tfont-weight: bold;")
        write("}")
        write("tr:nth-child(even) {")
        write("\tbackground-color: #f9f9f9;")
        write("}")
        write("caption {")
        write("\tfont-weight: bold;")
        write("\tmargin-bottom: 10px;")
        write("}")

    for outer_idx in range(10):
        with open(os.path.join(output_dir, f"esp_chr_{str(outer_idx).zfill(3)}.html"), "w") as fid:

            def write(string: str) -> None:
                fid.write(f"{string}\n")

            write("<!DOCTYPE html>")
            write('<html lang="en">')
            write("<head>")
            write('\t<meta charset="UTF-8">')
            write('\t<meta name="viewport" content="width=device-width, initial-scale=1.0">')
            write("\t<title>HTML Table Example</title>")
            write('\t<link rel="stylesheet" href="./styles.css">')
            write("</head>")

            write("<body>")
            write("<table>")
            for idx in range(10000):
                if idx % 10 == 0:
                    write("\t<tr>")

                write(f"\t\t<td>&amp;&#35;{str(outer_idx * 10000 + idx).zfill(4)};</td>")
                write(f"\t\t<td>&#{str(outer_idx * 10000 + idx).zfill(4)};</td>")

                if (idx + 1) % 10 == 0:
                    write("\t<tr>")
            write("</table>")
            write("</body>")
            write("</html>")


if __name__ == "__main__":
    main()
