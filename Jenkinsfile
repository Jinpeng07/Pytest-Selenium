def createVersion() {
    // 定义一个版本号作为当次构建的版本，输出结果 20191210175842_69
    return new Date().format('yyyyMMdd-HH:mm:ss') + "_${env.BUILD_ID}"
}
pipeline{
	agent any
	environment {
        _version = createVersion()
    }
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
             subject: 'pipeline demo result: ${env._version}',
             to: '18770766249@163.com'
        }
    }
}
