## BIN Lookup API

This API provides functionality to look up BIN (Bank Identification Number) information from a SQLite database.

### Installation

1. **Install dependencies:**

   ```bash
   pip install Flask sqlite3
   ```

2. **Database setup:**

   * Ensure you have a SQLite database named `bin_list_data.db` in the `/app` directory.
   * This database should have a table named `bin_list` with a column `BIN` containing the BIN numbers.

### Running the application

```bash
python app.py
```

The API will be running at `http://0.0.0.0:5000`.

### API Usage

#### Get a list of all BINs

* **Endpoint:** `/api/bins`
* **Method:** GET
* **Description:** Returns a list of all BINs in the database.

#### Get information about a specific BIN

* **Endpoint:** `/api/bin/<bin_number>`
* **Method:** GET
* **Description:** Returns information about the specified BIN. Only the first 6 characters of the BIN number are used for the lookup.
* **Parameters:**
    * `bin_number` (string): The BIN number to look up.

### Examples

```bash
# Get all BINs
curl http://localhost:5000/api/bins

# Get information about BIN 424242
curl http://localhost:5000/api/bin/424242
```

### Notes

* This API uses SQLite for data storage. For large production applications, consider using a more robust database such as PostgreSQL or MySQL.
* This API supports multithreading to handle multiple requests concurrently.

**If you have any questions or issues, please feel free to contact us.** 

