"""
GCMS CampusFlow v10 — Government College of Management Sciences, Sangota, Swat
Modular Flask application: each section is a separate Blueprint.
"""
import os
from flask import Flask, redirect, url_for

# Load .env (ANTHROPIC_API_KEY etc.)
try:
    from dotenv import load_dotenv
    load_dotenv(override=False)
except ImportError:
    pass

from core.database import init_db
from core.helpers  import inject_globals

# ── Blueprint imports ──────────────────────────────────────────────────────
from blueprints.auth           import auth_bp
from blueprints.dashboard      import dashboard_bp
from blueprints.student_portal import student_bp
from blueprints.students       import students_bp
from blueprints.attendance     import attendance_bp
from blueprints.examination    import examination_bp
from blueprints.datesheet      import datesheet_bp
from blueprints.payments       import payments_bp
from blueprints.settings       import settings_bp
from blueprints.notifications  import notifications_bp
from blueprints.chatbot        import chatbot_bp
from blueprints.pdf            import pdf_bp
from blueprints.ai_insights    import ai_insights_bp


def create_app():
    app = Flask(__name__, static_folder='static')
    app.secret_key = os.environ.get('SECRET_KEY', 'GCMS_CampusFlow_2026_Sangota_Swat')
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'uploads')
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Register context processor
    app.context_processor(inject_globals)

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(student_bp)
    app.register_blueprint(students_bp)
    app.register_blueprint(attendance_bp)
    app.register_blueprint(examination_bp)
    app.register_blueprint(datesheet_bp)
    app.register_blueprint(payments_bp)
    app.register_blueprint(settings_bp)
    app.register_blueprint(notifications_bp)
    app.register_blueprint(chatbot_bp)
    app.register_blueprint(pdf_bp)
    app.register_blueprint(ai_insights_bp)

    @app.route('/')
    def index():
        return redirect(url_for('auth.login'))

    return app


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        init_db()
    print("\n" + "="*60)
    print("  GCMS CampusFlow v10")
    print("  Government College of Management Sciences, Sangota Swat")
    print("  http://localhost:5000")
    print("  Admin: admin / admin123")
    print("="*60 + "\n")
    app.run(debug=True, port=5000)
