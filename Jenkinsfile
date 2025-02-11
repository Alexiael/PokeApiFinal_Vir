pipeline {
    agent any

    stages {
        stage('Debug Workspace') {
            steps {
                powershell '''
                Write-Host "MOSTRANDO CARPETA ACTUAL..."
                pwd
                Write-Host "LISTADO RECURSIVO..."
                ls -Recurse
                '''
            }
        }

        stage('Setup Python') {
            steps {
                powershell '''
                  # Creamos un entorno virtual
                  python -m venv venv

                  # Activamos el entorno virtual
                  .\\venv\\Scripts\\activate

                  # Actualizamos pip
                  python -m pip install --upgrade pip

                  # Instalamos las dependencias
                  pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests (Local)') {
            steps {
                powershell '''
                  # Activamos de nuevo el venv (nueva sesión de PowerShell)
                  .\\venv\\Scripts\\activate

                  # Ejecutamos pytest con reporte JUnit
                  pytest --junitxml=results.xml
                '''
            }
        }

        stage('Run Tests (Docker)') {
            steps {
                powershell '''
                  # Ejecutamos pytest dentro del contenedor Docker
                  docker run --rm my-fastapi-app pytest --junitxml=results_docker.xml
                '''
            }
        }

        stage('Publish Test Results') {
            steps {
                // Publicamos los reportes JUnit en Jenkins
                junit 'results.xml'
                junit 'results_docker.xml'
            }
        }
    }

    post {
        always {
            // Limpia el workspace al final
            cleanWs()
        }
        success {
            echo '¡Pipeline completado con éxito!'
        }
        failure {
            echo 'El pipeline ha fallado.'
        }
    }
}

