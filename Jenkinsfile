pipeline{
	agent any
	stages{
		stage("UI Automation Test"){
			steps{
			    bat 'pytest --html=./report/report.html --self-contained-html -sv'
			}
		}
	}
	post{
	}
}
