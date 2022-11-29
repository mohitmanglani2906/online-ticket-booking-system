from flask import Flask, request, render_template, jsonify, make_response
import json
import utils.sendEmail as se
import utils.connectWithMongo as cwm
import utils.helper as helper
from datetime import datetime

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/book-ticket', methods=['POST'])
def bookTicket():
    try:
        ticketRecord = json.loads(request.data.decode())
        booking_time = datetime.now().isoformat(timespec='milliseconds') + 'Z'
        ticketRecord['createdAt'] = booking_time
        ticketRecord['pnrRecords'] = helper.generetePNRNumber(ticketRecord)
        # print(ticketRecord)
        se.sendEmailSendgrid(ticketRecord)  # will implement letter if required
        cwm.saveData(record=ticketRecord, dbName='online-ticket-booking', tableName='bookingData')
        # print(record)
        res = make_response({"message": "success!"}, 200)
        return res
    except Exception as e:
        # print("Something went wrong", e.args)
        res = make_response({"message": "not success!"}, 204)
        return res


@app.route('/search-ticket-view', methods=['GET'])
def searchTicketView():
    return render_template('searchTicket.html')


@app.route('/search-ticket', methods=['POST'])
def searchTicketByPNR():
    try:
        pnrNumberJson = json.loads(request.data.decode())
        # print("pnr number", pnrNumberJson)
        ticketRecord = cwm.searchPNR(dbName='online-ticket-booking', tableName='bookingData',
                                     pnrRecord="#"+pnrNumberJson.get('pnrNumber'))
        if ticketRecord:
            ticketRecord.pop('_id')
            # print(pnrNumberJson, "\n", ticketRecord)
            res = make_response({"message": "success!", "data": ticketRecord}, 200)
        else:
            res = make_response({"message": "not success!"}, 204)
        return res
    except Exception as e:
        # print("Something went wrong", e)
        res = make_response({"message": "not success!"}, 500)
        return res

@app.route('/show-analytics')
def showAnalytics():
    return render_template('analytics.html')


@app.route('/cancel-ticket')
def cancelTicketView():
    return render_template('cancelTicket.html')


@app.route('/thank-you')
def thankYou():
    return render_template('thankYou.html')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)



