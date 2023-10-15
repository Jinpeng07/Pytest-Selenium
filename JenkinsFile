#声明
pipeline{
	agent-any #代表任意节点
	stages{   #阶段
		stage("UI Automation Test"){  #描述那个阶段
			steps{  #具体的任务步骤
			    bat 'pytest --html=./report/report.html --self-contained-html -sv'
			}
		}
	}
	post{ #任务完成后的处理，发邮件、展示报告等
	}
}
#在哪个节点、完成任务、完成后需要做的事情
