
import argparse

import requests
from colorama import Fore , Style ,init

init()


parser=argparse.ArgumentParser(description="my first parser")



parser.add_argument("-u","--urls",help="enter the u man",required=True)
parser.add_argument("-w","--wordlist",help="enter the u man",required=True)

arguments=parser.parse_args()
def Start_brute_attack():
    print(Fore.LIGHTBLUE_EX + "Starting Brute Forcing To " + arguments.urls)
    results = []  # collect (url, status_code) tuples here

    with open(arguments.wordlist, 'r') as wordlists:
        for words in wordlists:
            full_url = arguments.urls + "/" + words.strip()
            per_request = requests.get(full_url)
            status = per_request.status_code
            results.append((full_url, status))
            # Optional: print progress in terminal
            color = Fore.GREEN if status == 200 else Fore.RED
            print(color + f"{full_url} --> {str(status).ljust(15)}")

    return results



def generate_html_report(results, filename="report.html"):
    rows_html = ""
    for url, status in results:
        if status == 200:
            row_class = "status-200"
        elif status == 404:
            row_class = "status-404"
        else:
            row_class = "status-other"

        rows_html += f"""
            <tr class="{row_class}">
                <td>{url}</td>
                <td>{status}</td>
            </tr>
        """

    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Brute Force Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; padding: 20px; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            th {{ background-color: #f4f4f4; }}
            tr:nth-child(even) {{ background-color: #f9f9f9; }}
            .status-200 {{ background-color: #d4edda; }}  /* greenish */
            .status-404 {{ background-color: #f8d7da; }}  /* reddish */
            .status-other {{ background-color: #fff3cd; }} /* yellowish */
        </style>
    </head>
    <body>
        <h1>Brute Force Scan Results</h1>
        <table>
            <tr>
                <th>URL</th>
                <th>Status Code</th>
            </tr>
            {rows_html}
        </table>
    </body>
    </html>
    """

    with open(filename, "w") as f:
        f.write(full_html)

    print(f"✅ Report saved to {filename}")



if __name__ == "__main__":
    results = Start_brute_attack()
    generate_html_report(results)

