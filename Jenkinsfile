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
            emailext body: '''
             <html>
             <h1> total cases: ${TEST_COUNT, var="total"}</h1>
             <h1> pass cases: ${TEST_COUNT, var="pass"}</h1>
             <h1> fail cases: ${TEST_COUNT, var="fail"}</h1>
             </html>''',
             subject: 'pipeline demo result',
             to: '18770766249@163.com'
        }
    }
}
