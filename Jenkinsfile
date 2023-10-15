pipeline{
	agent any
	stages{
		stage("UI Automation Test"){
			steps{
			    bat 'pytest --html=./report/report.html --self-contained-html -sv --junitxml=./report/report.xml'
			}
		}
	}
	post {
    always {
            junit 'report/report.xml'
            emailext body: '''<html>
                                    <h1> total cases: ${TEST_COUNTS, var="total"}</h1>
                                    <h1> pass cases: ${TEST_COUNTS, var="pass"}</h1>
                                    <h1> fail cases: ${TEST_COUNTS, var="fail"}</h1>
                               </html>''',
             subject: 'pipeline demo result',
             to: '18770766249@163.com'
        }
    }
}
