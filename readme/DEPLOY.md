<h1 align="center">
  <img src="docker.jpeg"
    alt="Docker" width="200">
  <br>
   Deploy project with docker
  <br>
</h1>

<hr>

<p align="center">
  <a href="#What-we-will-have">What we will have</a> •
  <a href="#Prepare-your-server">Prepare your server</a> •
  <a href="#Deploy-to-server-with-docker">Deploy to server with docker</a> •
  <a href="#additional-material">Additional material</a>
</p>

## What we will have
- Project (djnango, celery, redis & postgres) will be run in docker containers
- Nginx will be configured (handling static and media files, cache & some security)
- Certbot will be configured to handle ssl and automatic updates


## Prepare your server
- [Initial Server Setup with Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-22-04)
- [How To Install and Use Docker on Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-22-04#step-1-installing-docker)


## Deploy to server with docker

NOTE: Some commands may need to be used with ```sudo```

1. Create new folder in you server
   ```bash
   mkdir projects
   ```

2. Go to a new folder
   ```bash
   cd projects
   ```

3. Clone git repo
   ```bash
   git clone https://github.com/mrKazzila/mini_online_store.git
   ```

4. Copy an example .env file because the real one is git ignored
   ```bash
   cp env/.env.example env/.env.project
   ```

5. Build project
   ```bash
   docker-compose -f docker-compose.prod.yaml up -d --build
   ```

6. Run certbot for creating ssl sert (update `your_email` & `your_domain`)
   ```bash
   docker-compose -f docker-compose.prod.yaml run --no-deps certbot \
   certonly --webroot --webroot-path=/var/www/certbot --agree-tos --no-eff-email --email your_email -d your_domain
   ```

7. Stop containers
   ```bash
   docker-compose -f docker-compose.prod.yaml down -v
   ```

8. Remove the # from the lines:
   <details>
   <summary>Step-by-step commands</summary>
   </details>

9. Build project with new settings
   ```bash
   docker-compose -f docker-compose.prod.yaml up -d --build
   ```

10. Step into django container
    ```bash
    docker-compose -f docker-compose.prod.yaml exec django bash
    ```

11. Make migrations
   ```bash
   python app/manage.py migrate --noinput
   ```

12. Collect static files
   ```bash
   python app/manage.py collectstatic --noinput
   ```

13. Create superuser
   ```bash
   python app/manage.py createsuperuser
   ```

14. Use product fixtures for add some goods into site
  - Firstly add categories
   ```python app/manage.py loaddata app/products/fixtures/categories.json```
  - Secondly add goods
   ```python app/manage.py loaddata app/products/fixtures/goods.json```

15. Add test purchase webhook (update domain (`your_domain`))
   ```bash
   stripe listen --forward-to your_domain/webhook/stripe/
   ```

16. Add images for goods from fixtures OR add new goods ;)


## Additional material
- [Docker doc](https://docs.docker.com/)
- [Stripe doc](https://stripe.com/docs/payments/checkout/fulfill-orders)
- [Certbot doc](https://eff-certbot.readthedocs.io/en/stable/intro.html)



<br>
<br>
<p align="center">
  <a href="https://github.com/mrKazzila">GitHub</a> •
  <a href="https://mrkazzila.github.io/resume/">Resume</a> •
  <a href="https://www.linkedin.com/in/i-kazakov/">LinkedIn</a>
</p>