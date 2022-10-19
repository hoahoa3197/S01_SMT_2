def Gol_CreateTable(nameTable):
    return "CREATE TABLE {TBLs}" \
           " (ID INTEGER PRIMARY KEY," \
           " Code VARCHAR(150) NOT NULL DEFAULT '0'," \
           " ValueINT INTEGER NOT NULL DEFAULT 0," \
           " ValueTXT TEXT  NOT NULL," \
           " Detail TEXT NULL," \
           " CreateDate DATETIME DEFAULT CURRENT_TIMESTAMP," \
           " Active BOOLEAN NOT NULL DEFAULT 1," \
           " Log TEXT NULL);".format(TBLs=nameTable)


def Gol_SelectVariable(nameTable, Code=None):
    if Code is None:
        return " SELECT * FROM {TBLs} ORDER BY ID DESC" \
            .format(TBLs=nameTable)
    else:
        return " SELECT * FROM {TBLs}" \
               " WHERE Code='{Code}'  ORDER BY ID DESC" \
            .format(TBLs=nameTable, Code=Code)


def Gol_UpdateVariable(nameTable, Code, ValueINT, ValueTXT):
    query = " UPDATE {TBLs} SET ValueINT='{ValueINT}',ValueTXT='{ValueTXT}' WHERE Code='{Code}'" \
        .format(TBLs=nameTable, Code=Code, ValueINT=ValueINT, ValueTXT=ValueTXT)
    return query


def Gol_InsertVariable(nameTable, Code, ValueINT, ValueTXT):
    return " INSERT INTO {TBLs} (Code,ValueINT,ValueTXT) VALUES ('{Code}','{ValueINT}','{ValueTXT}')" \
        .format(TBLs=nameTable, Code=Code, ValueINT=ValueINT, ValueTXT=ValueTXT)


def Setting_CreateTable(nameTable):
    return "CREATE TABLE {TBLs}" \
           " (ID INTEGER PRIMARY KEY," \
           " Code VARCHAR(150) NOT NULL DEFAULT '0'," \
           " Value TEXT  NOT NULL," \
           " ProductSoftID INTERGER," \
           " SoftwareID INTERGER," \
           " CreateDate DATETIME DEFAULT CURRENT_TIMESTAMP," \
           " CreateBy VARCHAR(150) NULL," \
           " UpdateDate DATETIME DEFAULT CURRENT_TIMESTAMP," \
           " UpdateBy VARCHAR(150) NULL," \
           " Active BOOLEAN NOT NULL DEFAULT 1," \
           " Log TEXT NULL);".format(TBLs=nameTable)


def Setting_SelectVariable(nameTable, Code=None):
    if Code is None:
        return " SELECT * FROM {TBLs} ORDER BY ID DESC" \
            .format(TBLs=nameTable)
    else:
        return " SELECT * FROM {TBLs}" \
               " WHERE Code='{Code}'  ORDER BY ID DESC" \
            .format(TBLs=nameTable, Code=Code)


def Setting_UpdateVariable(nameTable, Code, Value, Datetime):
    query = " UPDATE {TBLs} SET Value='{Value}', UpdateDate='{Datetime}' WHERE Code='{Code}'" \
        .format(TBLs=nameTable, Code=Code, Value=Value, Datetime=Datetime)
    return query


def Setting_InsertVariable(nameTable, Code, Value):
    return " INSERT INTO {TBLs} (Code,Value) VALUES ('{Code}','{Value}')" \
        .format(TBLs=nameTable, Code=Code, Value=Value)


def ListImage_CreateTable(nameTable):
    return "CREATE TABLE {TBLs}" \
           " (ID INTEGER PRIMARY KEY," \
           " Dir VARCHAR(150) NOT NULL DEFAULT '0'," \
           " FileName TEXT NOT NULL DEFAULT 0," \
           " Detail TEXT NULL," \
           " CreateDate DATETIME DEFAULT CURRENT_TIMESTAMP," \
           " ToServer BOOLEAN NOT NULL DEFAULT 1," \
           " Log TEXT NULL);".format(TBLs=nameTable)


def ListImage_SelectVariable(nameTable, ToServer=None):
    if ToServer is None:
        return " SELECT * FROM {TBLs} ORDER BY ID DESC" \
            .format(TBLs=nameTable)
    else:
        return " SELECT * FROM {TBLs}" \
               " WHERE ToServer='{ToServer}'  ORDER BY ID DESC" \
            .format(TBLs=nameTable, ToServer=ToServer)


def ListImage_UpdateVariable(nameTable, ID, ToServer):
    query = " UPDATE {TBLs} SET ToServer='{ToServer}' WHERE ID='{ID}'" \
        .format(TBLs=nameTable, ID=ID, ToServer=ToServer)
    return query


def ListImage_InsertVariable(nameTable, Dir, FileName):
    return " INSERT INTO {TBLs} (Dir,FileName) VALUES ('{Dir}','{FileName}')" \
        .format(TBLs=nameTable, Dir=Dir, FileName=FileName)
