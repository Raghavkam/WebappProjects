const express = require('express');
const sqlite3 = require('sqlite3').verbose();

const app = express();

const db = new sqlite3.Database('database.db');


function updateDatabase(name, newMagic) {
    const sql = `UPDATE characters SET c_magic = ? WHERE c_name = ?`;
    const params = [newMagic, name];
    return new Promise((resolve, reject) => {
        db.run(sql, params, function (err) {
            if (err) {
                reject(err);
            } else {
                resolve(this.changes);
            }
        });
    });
}


function retrieveData() {
    const sql = `SELECT * FROM characters`;
    return new Promise((resolve, reject) => {
        db.all(sql, [], (err, rows) => {
            if (err) {
                reject(err);
            } else {
                resolve(rows);
            }
        });
    });
}



async function main() {
    const updateResult = await updateDatabase('Archibald', 10);
    console.log(`Updated ${updateResult} rows.`);


    const data = await retrieveData();
    console.log("Retrieved data:");
    console.log(data);

    return data;

}


main()
