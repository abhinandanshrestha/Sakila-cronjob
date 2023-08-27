from components.execQuery import getResult
from components.createCSV import createCSV
from components.sendMail import sendMail

if __name__=='__main__':
    queryResult=getResult()
    createCSV(queryResult)
    sendMail()
