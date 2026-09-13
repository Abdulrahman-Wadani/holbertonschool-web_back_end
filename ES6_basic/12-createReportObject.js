export default function createReportObject(employeesList) {
    report = {
        'allEmployees': {...employeesList},
        'getNumberOfDepartments': () => Object.keys(employeesList).length
    }

}
