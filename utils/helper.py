import random

def generetePNRNumber(record: dict = None):
    pnrRecords = list()
    for i in range(int(record['noOfPassengers'])):
        pnrNumber = ''
        pnrNumber = record['sourcePlace'][0:3].lower() +"#" \
                    + record['destinationPlace'][0:3].lower() if len(record['sourcePlace']) >=3 and len(record['destinationPlace']) >=3 else \
                    record['sourcePlace'][0:2].lower() +"#" \
                    + record['destinationPlace'][0:2].lower()
        pnrNumber += '#' + record['date'].split('-')[-1]+record['date'].split('-')[-2]
        pnrNumber += '#' + record['createdAt'].split('T')[-1][0:2] + record['createdAt'].split('T')[-1][3:5]
        pnrNumber += '#' + str(random.random()).split('.')[-1][0:4]
        pnrRecords.append(pnrNumber)
    # print(pnrRecords)
    return pnrRecords











