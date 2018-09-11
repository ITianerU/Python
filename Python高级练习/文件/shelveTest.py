#用法和字典类似,只能存储.db文件,不支持多个应用并行写入
import shelve as shl
s = shl.open("laowang.db")
s["one"] = [1,2,3]
s["two"] = "不洗澡"
s.close()

#使用
sr = shl.open("laowang.db")
print(sr["one"])
print(sr["two"])

#强制写回 writeback=true
s2 = shl.open("laowang.db",writeback=True)
sone = s2["one"]
sone[1] = "死肥宅爱喝茶"
s2.close()

sr2 = shl.open("laowang.db")
print(sr2["one"])
sr2.close()

with shl.open("laowang.db",writeback=True) as f:
    print(f["one"])