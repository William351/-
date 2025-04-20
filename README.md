这是一个使用Selenium和GitHub Actions实现的朵朵校友圈(duoduo.link)自动签到脚本，每天自动执行签到操作。

使用说明
前置要求
GitHub账号

朵朵校友圈的有效Bearer Token

快速开始
Fork本仓库
点击右上角Fork按钮将此仓库复制到你的账号下

设置Secrets
在你的仓库设置中添加以下Secrets：

DUODUO_TOKEN: 你的朵朵校友圈Bearer Token

手动运行工作流
转到Actions标签页，选择"Duoduo Link Auto Signin"工作流，点击"Run workflow"手动触发

常见问题
Q: 如何获取我的Bearer Token?
A: 登录朵朵校友圈后，通过浏览器开发者工具查看应用程序（application）中localStorage中的auth-store对象。

Q: 签到失败怎么办?
A: 检查Actions日志中的错误信息，可能需要更新XPath定位器或令牌。