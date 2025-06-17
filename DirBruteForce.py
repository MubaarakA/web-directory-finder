import argparse

import requests
from colorama import Fore , Style ,init

init()

parser=argparse.ArgumentParser(description="my first parser")



parser.add_argument("-u","--urls",help="enter the u man",required=True)
parser.add_argument("-w","--wordlist",help="enter the u man",required=True)

arguments=parser.parse_args()


def Start_brute_attack():
    reports = []
    Found_status=[]
    print(Fore.LIGHTBLUE_EX+  "Starting Brute Forcing To " + arguments.urls)
    with open(arguments.wordlist, 'r') as wordlists:

        for words in wordlists:
            Full_url=arguments.urls+"/"+words.strip()
            Per_reqeust=requests.get(Full_url)
            reports.append([Per_reqeust.url,Per_reqeust.status_code])



            if Per_reqeust.status_code==200:
                status= str(Per_reqeust.status_code).ljust(15)
                Found_status.append([Per_reqeust.url, Per_reqeust.status_code])

                print(Fore.GREEN + Per_reqeust.url + " -->",status)
            status = str(Per_reqeust.status_code).ljust(15)
            print(Fore.RED + Per_reqeust.url + " -->", status)

        print(Fore.LIGHTBLUE_EX+ "Here Is Founded 200 Status Codes")
        for url,status in Found_status:
            print(Fore.GREEN + Per_reqeust.url + " -->",status)


        print()

    return reports ,Found_status





def Generate_Html_Report(reports,Found_status,filename="report.html"):
    rows_html=""
    for url ,status in reports:


        if status == 404:
            row_class ="red"
            rows_html+=f"""<tr class={row_class}> <td> {url}  </td> 
                            <td> {status}  </td>
         </tr>"""
        Rows200_html=""
        for url, status in Found_status:

            Rows200_html += f"""<tr class={"green"}> <td> {url}  </td> 
                                   <td> {status}  </td>
                </tr>"""
    full_html=f"""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    
     <style>
     th {{ background-color: #f4f4f4; }}
     body {{ font-family: Arial, sans-serif; padding: 20px; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        .green{{
            background-color: green;
            color:white
        }}
        .red{{
            background-color: rgb(188, 219, 188);
            color:black
        }}
    </style>
</head>
<body>
    <table border="1">
        <tr><th>Website</th>  
        <th>Status Code</th>
        </tr>
       {Rows200_html}

       {rows_html}
       
       


    </table>
</body>
</html>
"""


    with open(filename, "w") as f:
        f.write(full_html)

    print(f"✅ Report saved to {filename} in current pwd")

reports,Found_status=Start_brute_attack()
Generate_Html_Report(reports,Found_status)