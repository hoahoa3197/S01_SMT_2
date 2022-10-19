import subprocess
import os, base64

import Core.StringQuery as SQL
from Core.API import API
from Core.SQLiteDB import SQLiteDB


class GlobalCtrl:
    GlobalConf = 'conf_global'
    ProjectConf = 'conf_project'
    imgData = "List_data_image"
    CPUID = 'SD Software'

    def __init__(self):
        self.api = API()
        self.SQLite = SQLiteDB()
        if self.SQLite.tableExist(self.GlobalConf) == False:
            self.SQLite.executeSQL(SQL.Gol_CreateTable(self.GlobalConf))
        if self.SQLite.tableExist(self.ProjectConf) == False:
            self.SQLite.executeSQL(SQL.Setting_CreateTable(self.ProjectConf))
        if self.SQLite.tableExist(self.imgData) == False:
            self.SQLite.executeSQL(SQL.ListImage_CreateTable(self.imgData))

        # wmic bios get serialnumber
        self.CPUID = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
        # self.CPUID = "lsahflsafsdlf"

    def GlobalFromDB(self, Code=None):
        query = SQL.Gol_SelectVariable(self.GlobalConf, Code)
        data = self.SQLite.listObject(query)
        if data is None or len(data) == 0:
            sql = SQL.Gol_InsertVariable(self.GlobalConf, 'ProductID', '0', 'ProductName')
            sql += " ,('PartID', '0', 'PartName')"
            sql += " ,('LocationID', '0', 'LocationName')"
            sql += " ,('LineID', '0', 'LineName')"
            sql += " ,('StationID', '0', 'StationName')"
            sql += " ,('ToServer', '1','" + self.CPUID + "')"
            self.SQLite.executeSQL(sql)
            return self.SQLite.listObject(query)
        else:
            return data

    def GlobalFromAPI(self, projectCode):
        return self.api.getGlobal(self.CPUID, projectCode)
        # return self.api.Gol_UpdateVariable(projectCode, self.CPUID)

    def GlobalToDB(self, Code, ValueINT, ValueTXT):
        return self.SQLite.executeSQL(SQL.Gol_UpdateVariable(self.GlobalConf, Code, ValueINT, ValueTXT))
        # return self.SQLite.executeSQL(SQL.Gol_InsertVariable(self.GlobalConf, Code, ValueINT, ValueTXT))

    # def GlobalToAPI(self, projectCode,data):
    #     data = {'api_key': 'API_KEY',
    #             'api_data': 'API_DATA'}
    #     return self.api.getVariables(projectCode, self.CPUID)

    def SettingFromDB(self):
        query = SQL.Setting_SelectVariable(self.ProjectConf)
        data = self.SQLite.listObject(query)
        if data is None or len(data) == 0:
            sql = SQL.Setting_InsertVariable(self.ProjectConf, 'Threshold', '-1')
            sql += " ,('Exposure', '0')"
            sql += " ,('X_axis', '-1')"
            sql += " ,('COM_port', '0')"
            sql += " ,('ToServer', '1')"
            self.SQLite.executeSQL(sql)
            return self.SQLite.listObject(query)
        else:
            return data

    def SettingFromAPI(self, projectCode):
        return self.api.getVariables(projectCode, self.CPUID)

    def SettingToDB(self, Code, Value, DateTime):
        return self.SQLite.executeSQL(SQL.Setting_UpdateVariable(self.ProjectConf, Code, Value, DateTime))

    # save Image
    def InsertImageToDB(self, Dir, FileName):
        return self.SQLite.executeSQL(SQL.ListImage_InsertVariable(self.imgData, Dir, FileName))

    def UpdataImageToDB(self, ID, ToServer):
        return self.SQLite.executeSQL(SQL.ListImage_UpdateVariable(self.imgData, ID, ToServer))

    def ListImageFromDB(self):
        query = SQL.ListImage_SelectVariable(self.imgData, ToServer=1)
        data = self.SQLite.listObject(query)
        return data

    def readInfoSever(self):
        # print("[INFO] Preparing data...!")
        totalData = []
        package_dir = os.path.dirname(os.path.abspath(__file__))
        txtFile = os.path.join(package_dir, '../DefaultData/dataUpdateCode.txt')
        with open(txtFile, "r") as r:
            data = r.read()
            listData = data.split("\n")
            for i in range(len(listData)):
                str = listData[i]
                if str == "":
                    continue
                strBytes = str.encode("utf-8")
                strEncode = base64.b64decode(strBytes)
                strEncode = strEncode.decode("utf-8")
                data = strEncode.rstrip("\n")
                data = data.split(":")
                totalData.append(data[1])
        return totalData