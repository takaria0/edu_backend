import os
from edu_backend.base_apis import app # import loaded app

if __name__ == "__main__":
  app.run(debug=os.environ.get('DEBUG', True), host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))