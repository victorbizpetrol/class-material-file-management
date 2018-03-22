# Python / JSON TODOs with Pathlib

---
**WARNING:** This project is **Python 3 only**. If you want to use Python 2 you should install `pathlib2` manually; **NOT** recommended though.
---

# Install

```bash
$ mkvirtualenv todos -p /usr/bin/python3
$ pip install -r requirements.txt
```

# Usage

**General:**

```bash
$ python main.py --help
$ python main.py --debug
```

**List todos**
```bash
$ python main.py list 
$ python main.py list -s pending
$ python main.py list -s done
$ python main.py list -s all
```


**Create todos**
```bash
$ python main.py create "My TODO Task"
$ python main.py create "My TODO Task" -c "programming"
$ python main.py create "My TODO Task" -d "Much description, wow"
$ python main.py create "My TODO Task" -d "Much description, wow" -p "2018-03-05"
```

### Homework

The functionality built during class only includes listing and creating new todos. Your tasks include:

##### 1) Mark TODOs as done

The function `main.complete` should mark a TODO as done.

##### 2) Serialize in multiple formats

Include an extra option and refactor `TodoManager` to include multiple serializer formats. For example, JSON, XML, CSV, TOML, etc.

Can you think of a binary format? (check out [Protocol Buffers](https://en.wikipedia.org/wiki/Protocol_Buffers, [MessagePack](https://en.wikipedia.org/wiki/MessagePack) or [BSON](https://en.wikipedia.org/wiki/BSON))
