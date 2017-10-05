# Alembic Setup Process

## Requirements
  1. alembic
  2. mysqlclient
  
## Usage
  1. Open up the COM service directory.
  2. Activate the virtual environment for the service.
  3. `pip3 install alembic mysqlclient`.
  4. run `alembic init <com_service_migrations>`. It generates a file `alembic.ini` and folder named `<com_service_migrations>`.
  5. Update the sql url in alembic.ini as `sqlalchemy.url = mysql:://<user>:<pass>@localhost/<db_name>`.
  6. Create a migration script as `alembic revision -m "create employee table"`. It generates a file under versions in <com_service_migrations>.
  7. Update the empty `upgrade()` function with required migrations and empty `downgrade()` function with down revision if needed.
  8. Run `alembic upgrade head` to make migrations.
  9. create another migration as `alembic revision -m "Add joined date column"`.
  10. Run 'alembic upgrade head` to make migrations.
  11. Run `alembic downgrade -1` to undo the last migration. The number denotes the last migration scripts.
