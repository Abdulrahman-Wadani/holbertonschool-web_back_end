class HolbertonCourse {
    constructor(name, length, students) {
        if (typeof name !== String)
            throw TypeError("name must be string");
        if (typeof length !== Number)
            throw TypeError("length must be number");
        if (typeof students !== Array){
            throw TypeError("students must be array of strings");
        }
        for (let student of students){
                if (typeof student !== String){
                    throw TypeError("students must be array of strings");
            }
        this._name = name;
        this._length = length;
        this._students = students;
        }
    }

    get name() {
        return this._name;
    }
    set name(newName) {
        if (typeof newName !== String)
            throw TypeError("name must be string");
        this._name = newName;  
    }
    get length() {
        return this._length;
    }
    set length(newLength) {
        if (typeof newLength !== String)
            throw TypeError("newLength must be Number");
        this._length = newLength;  
    }
    get students() {
        return this._students;
    }
    set students(newStudents) {
        if (typeof newStudents !== Array){
            throw TypeError("students must be array of strings");
        }
        for (let student of students){
                if (typeof student !== String){
                    throw TypeError("students must be array of strings");
            }  
        }
        this.students = newStudents;
}
}

