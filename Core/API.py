import json
import urllib.request

# import requests


class API:
    # ListUrlGet = ['http://10.228.14.26:17715/', 'http://10.228.16.77:17715/']
    ListUrl = ['http://10.228.14.26:17716/', 'http://10.228.16.77:17715/']
    Url = None
    subUrl = 'SFCInfo/'
    urlProduct = 'OutputProject'
    urlPart = 'OutputPart/'
    urlLocation = 'OutputLocation/'
    urlLine = 'OutputLine/'
    urlStation = 'OutputStation/'

    urlGetGlobal = 'Info/'
    urlPostGlobal = 'Datainfo'
    urlGetVariables = 'VariablesSoftware/'
    urlPostVariables = 'Variables'

    # Check in URL Office or SFC
    def APIurl(self, subLink, listURL):
        # if self.Url is None:
        for url in listURL:
            request = urllib.request.Request(url)
            try:
                response = urllib.request.urlopen(request)
                self.Url = url
                break
            except urllib.error.HTTPError as e:
                self.Url = None
                continue
            except urllib.error.URLError as e:
                self.Url = None
                continue
        if self.Url is None:
            return None
        else:
            return self.Url + self.subUrl + subLink

    # The Function get data from API
    def getAPI(self, url, params=None):
        # PARAMS = {'data': data}
        if url is None:
            return None
        try:
            if params is None:
                response = requests.get(url=url)
            else:
                response = requests.get(url=url, params=params)
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except:
            return None

    def postAPI(self, url, data):
        # data = {'api_key': 'API_KEY',
        #         'api_data': 'API_DATA'}
        if url is None:
            return None
        try:
            jsondata = json.dumps(data)
            jsondataasbytes = jsondata.encode('utf-8')
            response = requests.post(url=url, data=jsondataasbytes)
            print(response.status_code)
            print(response.json())
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 502:
                return "Error 502 Bad Gateway"
            else:
                return None
        except Exception as e:
            print("[ERROR] postAPI", e)
            return None

    def getListProduct(self):
        url = self.APIurl(self.urlProduct, self.ListUrl)
        return self.getAPI(url)

    def getListPart(self, productID):
        url = self.APIurl(self.urlPart, self.ListUrl)
        # data = {'ProductID': productID}
        # return self.getAPI(url, data)
        urlData = url + str(productID)
        return self.getAPI(urlData)

    def getListLocation(self, productID, partID):
        url = self.APIurl(self.urlLocation, self.ListUrl)
        # data = {'ProductID': productID,
        #         'PartID': partID}
        # return self.getAPI(url, data)
        urlData = url + str(productID) + "," + str(partID)
        return self.getAPI(urlData)

    def getListLine(self, productID, partID, LocationID):
        url = self.APIurl(self.urlLine, self.ListUrl)
        # data = {'ProductID': productID,
        #         'PartID': partID,
        #         'LocationID': LocationID,
        #         }
        # return self.getAPI(url, data)
        urlData = url + str(productID) + "," + str(partID) + "," + str(LocationID)
        return self.getAPI(urlData)

    def getListStation(self, productID, partID, LocationID, LineID):
        url = self.APIurl(self.urlStation, self.ListUrl)
        # data = {'ProductID': productID,
        #         'PartID': partID,
        #         'LocationID': LocationID,
        #         'LineID': LineID,
        #         }
        # return self.getAPI(url, data)
        urlData = url + str(productID) + "," + str(partID) + "," + str(LocationID) + "," + str(LineID)
        return self.getAPI(urlData)

    def getGlobal(self, CPUID, ProjectCode):
        url = self.APIurl(self.urlGetGlobal, self.ListUrl)
        # data = {'CPUID': CPUID,
        #         'ProjectCode': ProjectCode,
        #         }
        # return self.getAPI(url, data)
        urlData = url + str(ProjectCode) + "," + str(CPUID)
        return self.getAPI(urlData)

    def postGlobal(self, CPUID, ProjectCode, ProductID, PartID, LocationID, LineID, StationID):
        url = self.APIurl(self.urlPostGlobal, self.ListUrl)
        print("URL Post Glo", url)
        data = {
            "CPUID": CPUID,
            "ProjectCode": ProjectCode,
            "ProductID": ProductID,
            "PartID": PartID,
            "LocationID": LocationID,
            "LineID": LineID,
            "StationID": StationID
        }
        return self.postAPI(url, data)

    # The function Get variable for
    def getVariables(self, projectCode, CPUID):
        url = self.APIurl(self.urlGetVariables, self.ListUrl)
        # data = {'CPUID': CPUID,
        #         'ProjectCode': projectCode,
        #         }
        # return self.getAPI(url, data)
        urlData = url + str(projectCode) + "," + str(CPUID)
        return self.getAPI(urlData)

    def postVariables(self, projectCode, CPUID, ThresholdVal, ExposureVal, X_axisVal, COMportName):
        url = self.APIurl(self.urlPostVariables, self.ListUrl)
        print("URL Post Val", url)
        data = {"Threshold": ThresholdVal,
                "Exposure": ExposureVal,
                "X_axis": X_axisVal,
                "COM_port": COMportName
                }
        res = None
        for i in data.items():
            postData = {"CPUID": CPUID,
                        "ProjectCode": projectCode,
                        "Code": i[0],
                        "Value": i[1]}
            print("Post status: ", postData)
            res = self.postAPI(url, postData)
            if res != True:
                break
        return res


if __name__ == "__main__":
    import datetime

    CPUID = "EE0F8A07-EDAF-586E-8E6B-1A4B65C2C367"
    data = [['Threshold', 20, datetime.datetime(2020, 12, 1, 14, 32, 25, 858336)],
            ['X_axis', 25, datetime.datetime(2020, 12, 1, 14, 32, 25, 858336)]]
    api = API()
    # a = api.postVariables("MLB_link_ST010", CPUID, 20, -5, 20)
    # print(a)
    # a = api.postGlobal(CPUID, "MLB_link_ST010", 1, 5, 7, 76, 1)
    # print(a, "Info")
    dataVal = api.getVariables("MLB_link_ST010", CPUID)
    print(dataVal)
    # print(data, type(data))
    dataGol = api.getGlobal(CPUID, "MLB_link_ST010")
    print(dataGol)
