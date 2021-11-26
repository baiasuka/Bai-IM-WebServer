JOBS = [
    # ===============计划任务配置文件= id不能一样======================
    # {
    #         # 每5分钟执行一次 评论及评论回复
    #         'id': 'job5',
    #         'func': 'scheduler_task.every_less_than_hour:comment_push',
    #         'args': '',
    #         'trigger': {
    #             # 'type': 'interval',
    #             # 'minutes': 2
    #             'type': 'cron',
    #             'minute': "1,6,11,16,21,26,31,36,41,46,51,56"
    #         }
    #     },
    # ==================样例分界线===================
]
SCHEDULER_API_ENABLED = True
