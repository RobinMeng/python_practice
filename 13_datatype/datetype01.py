## json 处理

import json

json_text = """
{
  "system_info": {
    "name": "用户管理系统",
    "version": "2.1.0",
    "last_updated": "2024-01-15",
    "active": true
  },
  "users": [
    {
      "id": 1001,
      "personal_info": {
        "name": "张三",
        "age": 28,
        "email": "zhangsan@example.com",
        "phone": "+86-138-0011-0011",
        "is_verified": true
      },
      "employment": {
        "company": "科技无限公司",
        "department": "研发部",
        "position": "高级工程师",
        "salary": 25000.50,
        "start_date": "2021-03-15"
      },
      "skills": ["Python", "JavaScript", "Docker", "MySQL"],
      "preferences": {
        "theme": "dark",
        "notifications": true,
        "language": "zh-CN"
      }
    },
    {
      "id": 1002,
      "personal_info": {
        "name": "李四",
        "age": 25,
        "email": "lisi@test.org",
        "phone": "+86-139-0022-0022",
        "is_verified": false
      },
      "employment": {
        "company": "数据智能科技",
        "department": "市场部",
        "position": "市场专员",
        "salary": 18000.00,
        "start_date": "2022-08-01"
      },
      "skills": ["市场营销", "数据分析", "英语", "PPT"],
      "preferences": {
        "theme": "light",
        "notifications": false,
        "language": "en-US"
      }
    },
    {
      "id": 1003,
      "personal_info": {
        "name": "王五",
        "age": 32,
        "email": "wangwu@company.com",
        "phone": null,
        "is_verified": true
      },
      "employment": {
        "company": "创新软件",
        "department": "产品部",
        "position": "产品经理",
        "salary": 32000.75,
        "start_date": "2019-11-20"
      },
      "skills": ["产品设计", "Axure", "项目管理", "用户研究"],
      "preferences": {
        "theme": "auto",
        "notifications": true,
        "language": "zh-CN"
      }
    }
  ],
  "statistics": {
    "total_users": 3,
    "average_age": 28.3,
    "verified_users": 2,
    "departments": ["研发部", "市场部", "产品部"],
    "salary_range": {
      "min": 18000.00,
      "max": 32000.75,
      "average": 25033.75
    }
  },
  "tags": ["employee", "test_data", "v2.1"]
}
"""

## 字符串转换为json
json_dict = json.loads(json_text)

print(type(json_dict))
print(json_dict)
print(json_dict['system_info'])
print(json_dict.get("system_info1", "test"))

## json 转换为字符串

json_dict2 = {
    "name": "test",
    "age": 19,
    "hobby": ["game", "running"]
}

json_str = json.dumps(json_dict2)
print(json_str)
print(type(json_str))
