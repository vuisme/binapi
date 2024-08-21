## BIN Lookup API

This API provides functionality to look up BIN (Bank Identification Number) information from a SQLite database.

### Installation Manual

1. **Install dependencies:**

   ```bash
   pip install Flask sqlite3
   ```

2. **Database setup:**

   * Ensure you have a SQLite database named `bin_list_data.db` in the `/app` directory.

### Running the application

```bash
python app.py
```

## Running with Docker

### 1. Build the Docker image (Option)
Clone project and build

```bash
docker build -t bin-lookup-api .
```
### 2.1 Run with my Build

```bash
docker run -d -p 5000:5000 --name bin-lookup-container cpanel10x/binbase
```

### 2.2 Run your build

```bash
docker run -d -p 5000:5000 --name bin-lookup-container bin-lookup-api
```

This will start the container in detached mode, map port 5000 from the container to port 5000 on your host machine, and name the container `bin-lookup-container`.

### Additional Docker commands

* **Stop the container:**

  ```bash
  docker stop bin-lookup-container
  ```

* **Start the container:**

  ```bash
  docker start bin-lookup-container
  ```

* **View container logs:**

  ```bash
  docker logs bin-lookup-container
  ```

**Make sure you have Docker installed and running on your machine before following these instructions.**

**Remember to replace `bin-lookup-api` with the actual name you gave your Docker image if it's different.**

The API will be running at `http://0.0.0.0:5000`.

### API Usage

#### Get information about a specific BIN

* **Endpoint:** `/api/bin/<bin_number>`
* **Method:** GET
* **Description:** Returns information about the specified BIN. Only the first 6 characters of the BIN number are used for the lookup.
* **Parameters:**
    * `bin_number` (string): The BIN number to look up.

### Examples

```bash
# Get information about BIN 424242
curl http://localhost:5000/api/bin/424242
```

### Notes

* This API uses SQLite for data storage. For large production applications, consider using a more robust database such as PostgreSQL or MySQL.
* This API supports multithreading to handle multiple requests concurrently.

**If you have any questions or issues, please feel free to contact us.** 

