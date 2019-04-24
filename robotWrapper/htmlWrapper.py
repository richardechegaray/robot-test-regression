import subprocess
from datetime import datetime
import os
import sys
import getopt


outputdir = 'C:/Users/rechegaray/Desktop/robotWrapper/testResults'

def run(amount_of_times, f):

    if (amount_of_times == 1) :

        i = (datetime.now())
        base = str((i.strftime("%b")) + (i.strftime("%d")) + '_'
               + (i.strftime("%y")) + 'at' + (i.strftime("%H")) + (i.strftime("%M")))

        log_name = base + '_l' + '.html'
        report_name = base + '_r' + '.html'
        output_name = base + '_o' + '.xml'
        commandList = ['robot', '--outputdir', outputdir + '/Logs',
                      '--log', log_name, '--report', report_name, '--output', output_name, 'tests']
        subprocess.run(commandList)

    else :
        for x in range (amount_of_times):
            i = (datetime.now())
            base = str((i.strftime("%b")) + (i.strftime("%d")) + '_'
                + (i.strftime("%y")) + 'at' + (i.strftime("%H")) + (i.strftime("%M")))

            log_name = base + '_l' + str(x+1) + '.html'
            report_name = base + '_r' + str(x+1) + '.html'
            output_name = base + '_o' + str(x+1) + '.xml'
            commandList = ['robot', '--outputdir', outputdir + '/Logs',
                          '--log', log_name, '--report', report_name, '--output', output_name, 'tests']
            subprocess.run(commandList)


def gen_header(f):
     f.write('<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\" \"http://www.w3.org/TR/html4/loose.dtd\">   ' + '\n')
     f.write('<html>                                                                                                       ' + '\n')
     f.write('    <head>                                                                                                   ' + '\n')
     f.write('        <title>TEST</title>                                                                                  ' + '\n')
     f.write('        <style type="text/css">                                                                              ' + '\n')
     f.write('            body {                                                                                           ' + '\n')
     f.write('                font-weight: 200;                                                                            ' + '\n')
     f.write('                font-size: 10px;                                                                             ' + '\n')
     f.write('            }                                                                                                ' + '\n')
     f.write('            .header {                                                                                        ' + '\n')
     f.write('                font-size: 20px;                                                                             ' + '\n')
     f.write('                font-weight: 100;                                                                            ' + '\n')
     f.write('                text-align: left;                                                                            ' + '\n')
     f.write('            }                                                                                                ' + '\n')
     f.write('            .title {                                                                                         ' + '\n')
     f.write('                font-size: 22px;                                                                             ' + '\n')
     f.write('                font-weight: 100;                                                                            ' + '\n')
     f.write('               /* text-align: right;*/                                                                       ' + '\n')
     f.write('               padding: 10px 20px 0px 20px;                                                                  ' + '\n')
     f.write('            }                                                                                                ' + '\n')
     f.write('            .title span {                                                                                    ' + '\n')
     f.write('                color: #007cae;                                                                              ' + '\n')
     f.write('            }                                                                                                ' + '\n')
     f.write('            .details {                                                                                       ' + '\n')
     f.write('                padding: 5px 5px 0px 5px;                                                                    ' + '\n')
     f.write('                text-align: left !important;                                                                 ' + '\n')
     f.write('                /*margin-left: 40%;*/                                                                        ' + '\n')
     f.write('            }                                                                                                ' + '\n')
     f.write('                                                                                                             ' + '\n')
     f.write('            u {                                                                                              ' + '\n')
     f.write('                text-decoration: underline;                                                                  ' + '\n')
     f.write('            }                                                                                                ' + '\n')
     f.write('                                                                                                             ' + '\n')
     f.write('            table.table1 {                                                                                   ' + '\n')
     f.write('              border: 1px solid black;                                                                       ' + '\n')
     f.write('              font-size: 12px;                                                                               ' + '\n')
     f.write('                                                                                                             ' + '\n')
     f.write('                                                                                                             ' + '\n')
     f.write('                                                                                                             ' + '\n')
     f.write('                                                                                                             ' + '\n')
     f.write('            }                                                                                                ' + '\n')
     f.write('            table.table1 th {                                                                                ' + '\n')
     f.write('              border: 1px solid black;                                                                       ' + '\n')
     f.write('              font-size: 12px;                                                                               ' + '\n')
     f.write('            }                                                                                                ' + '\n')
     f.write('            table.table1 tr {                                                                                ' + '\n')
     f.write('              border: 1px solid black;                                                                       ' + '\n')
     f.write('              font-size: 12px;                                                                               ' + '\n')
     f.write('                                                                                                             ' + '\n')
     f.write('            }                                                                                                ' + '\n')
     f.write('            table.table1 td {                                                                                ' + '\n')
     f.write('              border: 1px solid black;                                                                       ' + '\n')
     f.write('              font-size: 12px;                                                                               ' + '\n')
     f.write('            }                                                                                                ' + '\n')
     f.write('                                                                                                             ' + '\n')
     f.write('                                                                                                             ' + '\n')
     f.write('            }                                                                                                ' + '\n')
     f.write('                                                                                                             ' + '\n')
     f.write('                                                                                                             ' + '\n')
     f.write('        </style>                                                                                             ' + '\n')
     f.write('    </head>                                                                                                  ' + '\n')
     f.write('    <body>                                                                                                   ' + '\n')
     f.write('       <div class=\'header\'>                                                                                ' + '\n')
     f.write('            <class=\'title\'>ROBOT FW Test Results                                                            ' + '\n')
     f.write('       </div>                                                                                                ' + '\n')
     f.write('        <table  class=\"table1\" >                                                                           ' + '\n')
     f.write('         <tr>                                                                                                ' + '\n')
     f.write('            <th>Date</th>                                                                                    ' + '\n')
     f.write('            <th>Time</th>                                                                                    ' + '\n')
     f.write('            <th>FW Version</th>                                                                              ' + '\n')
     f.write('            <th>Passed</th>                                                                                  ' + '\n')
     f.write('            <th>Failed</th>                                                                                  ' + '\n')
     f.write('            <th>Results</th>                                                                                 ' + '\n')
     f.write('        </tr>                                                                                                ' + '\n')

def html_init():
    htmlFileName = outputdir + '/robot_fw_test.html'
    f = open(htmlFileName, 'w')
    gen_header(f)
    return f

def add_table_row(f, row):
    f.write('         <tr>                                                   ' + '\n')
    f.write('            <td>' + row['DATE']                           +  ' </td> \n')
    f.write('            <td>' + row['TIME']                           +   '</td> \n')
    f.write('            <td>' + row['FW_VER']                         +  ' </td> \n')
    f.write('            <td>' + str(row['PASSED'])                    +  ' </td> \n')
    f.write('            <td>' + str(row['FAILED'])                    +  ' </td> \n')
    f.write('            <td> <a href=' + row['RESULTS']  +  '> Report </a> </td> \n')
    f.write('        </tr>                                                   ' + '\n')

def close_file(f):
    f.write('           </table>                    ' + '\n')
    f.write('      </div>                           ' + '\n')
    f.write(' </body>                               ' + '\n')
    f.write('</html>                                ' + '\n')
    f.write('</html>' + '\n')
    f.close()

def populate_file(data_root, outFile):

    #if data_root exists
    if not os.path.isdir(data_root):
        print('ERROR dir_walk: DATA_ROOT does not exist:', data_root)
        return

    # print('Traversing Dir Structure of...: ' + data_root)
    reportList = []

    for dirPath, dNames, fNames in os.walk(data_root):
        for f in fNames:
            if f.endswith('.html') and '_r' in f:
                reportList.append(f)

    reportList.sort(reverse = True)

    for i in range(len(reportList)):
        r = {'DATE': reportList[i][0:3] + '. ' + reportList[i][3:5] + ', 20'+ reportList[i][6:8],
             'TIME': reportList[i][10:12] + ':' + reportList[i][12:14],
             'FW_VER':'TBD',
             'PASSED':'TBD',
             'FAILED':'TBD',
             'RESULTS':outputdir + '/Logs/' + reportList[i]}

        add_table_row(outFile, r)

#outputdir = 'C:/Users/rechegaray/Desktop/robotWrapper/testResults'
f = html_init()
run(1, f)  #amount of times to run the robot framework
populate_file(outputdir + '/Logs', f)
print('\nSuccess!')
print('\nView logs at: ' + outputdir + '/robot_fw_test.html')
close_file(f)
