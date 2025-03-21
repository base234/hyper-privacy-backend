# data/sample_ads.py

def get_sample_ads():
    """
    Returns a list of 80 sample ads for the hackathon demo.
    Returns:
        list: A list of dictionaries containing ad content and metadata
    """
    return [
        # Technology ads
        {
            "content": "Get 50% off on the latest tech gadgets and smartphones! New models with AI features.",
            "metadata": {"category": "technology", "target_audience": "tech-savvy"},
        },
        {
            "content": "Smart home devices to automate your daily routines. Control everything from your phone!",
            "metadata": {"category": "technology", "target_audience": "homeowners"},
        },
        {
            "content": "Ultra-thin laptops with 20-hour battery life. Perfect for professionals on the go.",
            "metadata": {"category": "technology", "target_audience": "professionals"},
        },
        {
            "content": "Gaming PCs built for maximum performance. Experience games like never before!",
            "metadata": {"category": "technology", "target_audience": "gamers"},
        },
        {
            "content": "Noise-cancelling headphones for immersive audio experience. Work or relax in peace.",
            "metadata": {"category": "technology", "target_audience": "commuters"},
        },
        {
            "content": "Smartwatches that monitor your health 24/7. Stay connected and stay healthy.",
            "metadata": {
                "category": "technology",
                "target_audience": "health-conscious",
            },
        },
        {
            "content": "Refurbished electronics at 70% off retail price. Quality guaranteed with 1-year warranty.",
            "metadata": {
                "category": "technology",
                "target_audience": "budget-shoppers",
            },
        },
        {
            "content": "Virtual reality headsets for immersive gaming and entertainment. Enter new worlds!",
            "metadata": {
                "category": "technology",
                "target_audience": "entertainment-seekers",
            },
        },
        # Health ads
        {
            "content": "Healthy organic food delivery service. First week free! Fresh ingredients delivered to your door.",
            "metadata": {"category": "health", "target_audience": "health-conscious"},
        },
        {
            "content": "New fitness app with personalized workout plans and nutrition advice. Stay fit and healthy!",
            "metadata": {
                "category": "health",
                "target_audience": "fitness-enthusiasts",
            },
        },
        {
            "content": "Premium vitamin supplements formulated by doctors. Support your immune system naturally.",
            "metadata": {"category": "health", "target_audience": "wellness-focused"},
        },
        {
            "content": "Plant-based protein powders for muscle recovery and growth. 100% natural ingredients.",
            "metadata": {"category": "health", "target_audience": "vegan-athletes"},
        },
        {
            "content": "Sleep tracking technology to improve your rest quality. Wake up refreshed every day.",
            "metadata": {"category": "health", "target_audience": "busy-professionals"},
        },
        {
            "content": "Mental wellness app with guided meditation and stress reduction exercises. Find your calm.",
            "metadata": {"category": "health", "target_audience": "stress-sufferers"},
        },
        {
            "content": "Ergonomic office chairs designed by orthopedic specialists. Prevent back pain while you work.",
            "metadata": {"category": "health", "target_audience": "remote-workers"},
        },
        {
            "content": "Air purifiers that remove 99.97% of allergens. Breathe cleaner air at home.",
            "metadata": {"category": "health", "target_audience": "allergy-sufferers"},
        },
        # Education ads
        {
            "content": "Online courses on data science and machine learning at discounted prices. Learn from industry experts.",
            "metadata": {"category": "education", "target_audience": "learners"},
        },
        {
            "content": "Language learning platform with native speakers. Become fluent in just 10 minutes a day.",
            "metadata": {
                "category": "education",
                "target_audience": "language-learners",
            },
        },
        {
            "content": "Interactive coding bootcamp for beginners. From zero to hired in 6 months.",
            "metadata": {"category": "education", "target_audience": "career-changers"},
        },
        {
            "content": "Professional certification courses recognized worldwide. Upgrade your credentials today.",
            "metadata": {
                "category": "education",
                "target_audience": "career-advancers",
            },
        },
        {
            "content": "Creative writing workshops led by bestselling authors. Unleash your storytelling potential.",
            "metadata": {"category": "education", "target_audience": "creative-types"},
        },
        {
            "content": "Online music lessons with personalized feedback. Learn any instrument from home.",
            "metadata": {
                "category": "education",
                "target_audience": "music-enthusiasts",
            },
        },
        {
            "content": "Educational toys that make STEM learning fun for kids. Playtime with purpose.",
            "metadata": {"category": "education", "target_audience": "parents"},
        },
        {
            "content": "Digital art and design courses with industry-standard tools. Portfolio-ready projects included.",
            "metadata": {"category": "education", "target_audience": "designers"},
        },
        # Travel ads
        {
            "content": "Travel packages to exotic destinations. Book now and save! Experience the adventure of a lifetime.",
            "metadata": {"category": "travel", "target_audience": "travelers"},
        },
        {
            "content": "Family-friendly vacation packages with activities for all ages. Create lasting memories together!",
            "metadata": {"category": "travel", "target_audience": "families"},
        },
        {
            "content": "Luxury cruise deals with all-inclusive packages. Sail the seas in style and comfort.",
            "metadata": {"category": "travel", "target_audience": "luxury-seekers"},
        },
        {
            "content": "Adventure tourism experiences: hiking, rafting, and climbing in pristine wilderness areas.",
            "metadata": {"category": "travel", "target_audience": "adventure-seekers"},
        },
        {
            "content": "Budget-friendly backpacking tours across Europe. See more for less!",
            "metadata": {"category": "travel", "target_audience": "young-travelers"},
        },
        {
            "content": "Eco-tourism destinations that support conservation efforts. Travel with purpose.",
            "metadata": {"category": "travel", "target_audience": "eco-conscious"},
        },
        {
            "content": "Cultural immersion trips with local guides. Experience authentic traditions and cuisine.",
            "metadata": {
                "category": "travel",
                "target_audience": "culture-enthusiasts",
            },
        },
        {
            "content": "Remote work retreats in beautiful locations. Change your office view!",
            "metadata": {"category": "travel", "target_audience": "digital-nomads"},
        },
        # Fashion ads
        {
            "content": "Sustainable fashion brands with eco-friendly materials. Stylish and good for the planet!",
            "metadata": {"category": "fashion", "target_audience": "eco-conscious"},
        },
        {
            "content": "Designer clothing sale - up to 70% off this season's collection. Look your best for less.",
            "metadata": {"category": "fashion", "target_audience": "fashion-forward"},
        },
        {
            "content": "Handcrafted jewelry made from ethically sourced materials. Unique pieces for every occasion.",
            "metadata": {"category": "fashion", "target_audience": "jewelry-lovers"},
        },
        {
            "content": "Performance athletic wear with moisture-wicking technology. Train harder, stay comfortable.",
            "metadata": {"category": "fashion", "target_audience": "athletes"},
        },
        {
            "content": "Vintage and second-hand designer finds. Sustainable fashion with unique style.",
            "metadata": {
                "category": "fashion",
                "target_audience": "vintage-enthusiasts",
            },
        },
        {
            "content": "Custom-tailored suits at off-the-rack prices. Look sharp at your next meeting.",
            "metadata": {
                "category": "fashion",
                "target_audience": "business-professionals",
            },
        },
        {
            "content": "Weather-resistant outerwear for outdoor adventures. Stay dry in any conditions.",
            "metadata": {
                "category": "fashion",
                "target_audience": "outdoor-enthusiasts",
            },
        },
        {
            "content": "Affordable fashion subscription box curated to your style. Refresh your wardrobe monthly.",
            "metadata": {"category": "fashion", "target_audience": "style-conscious"},
        },
        # Finance ads
        {
            "content": "Investment opportunities in renewable energy. Grow your portfolio while supporting green initiatives.",
            "metadata": {"category": "finance", "target_audience": "investors"},
        },
        {
            "content": "Professional financial advisory services. Plan your future with expert guidance.",
            "metadata": {"category": "finance", "target_audience": "professionals"},
        },
        {
            "content": "Zero-fee checking accounts with high-interest savings. Make your money work harder.",
            "metadata": {"category": "finance", "target_audience": "savers"},
        },
        {
            "content": "Automated investment platforms with AI-powered strategies. Investing made simple.",
            "metadata": {
                "category": "finance",
                "target_audience": "beginner-investors",
            },
        },
        {
            "content": "Student loan refinancing at record-low rates. Save thousands over the life of your loan.",
            "metadata": {"category": "finance", "target_audience": "graduates"},
        },
        {
            "content": "Retirement planning services tailored to your goals. Secure your future today.",
            "metadata": {"category": "finance", "target_audience": "pre-retirees"},
        },
        {
            "content": "Credit cards with exceptional travel rewards. Earn points on every purchase.",
            "metadata": {
                "category": "finance",
                "target_audience": "frequent-travelers",
            },
        },
        {
            "content": "Business loans with flexible terms for startups and small businesses. Fuel your growth.",
            "metadata": {"category": "finance", "target_audience": "entrepreneurs"},
        },
        # Entertainment ads
        {
            "content": "Streaming service with exclusive shows and movies. First month free trial!",
            "metadata": {"category": "entertainment", "target_audience": "streamers"},
        },
        {
            "content": "Live concert tickets for popular artists. Early bird pricing available now.",
            "metadata": {
                "category": "entertainment",
                "target_audience": "music-lovers",
            },
        },
        {
            "content": "Immersive escape room experiences for friends and family. Can you solve the puzzle?",
            "metadata": {
                "category": "entertainment",
                "target_audience": "thrill-seekers",
            },
        },
        {
            "content": "Digital book subscription with unlimited reading. Thousands of titles at your fingertips.",
            "metadata": {"category": "entertainment", "target_audience": "readers"},
        },
        {
            "content": "Board game collections for game nights. Bring friends together with strategy and fun.",
            "metadata": {
                "category": "entertainment",
                "target_audience": "social-gamers",
            },
        },
        {
            "content": "Virtual cooking classes with celebrity chefs. Learn gourmet techniques at home.",
            "metadata": {"category": "entertainment", "target_audience": "foodies"},
        },
        {
            "content": "Premium podcast subscriptions with ad-free listening. Exclusive content for subscribers.",
            "metadata": {
                "category": "entertainment",
                "target_audience": "podcast-listeners",
            },
        },
        {
            "content": "Theme park annual passes with special member events. Unlimited adventures all year.",
            "metadata": {"category": "entertainment", "target_audience": "families"},
        },
        # Home & Garden ads
        {
            "content": "Modular furniture systems for flexible living spaces. Adapt your home to your needs.",
            "metadata": {"category": "home", "target_audience": "homeowners"},
        },
        {
            "content": "Indoor gardening kits for growing herbs and vegetables. Fresh produce year-round.",
            "metadata": {"category": "home", "target_audience": "urban-gardeners"},
        },
        {
            "content": "Energy-efficient appliances that reduce your utility bills. Save money while saving the planet.",
            "metadata": {"category": "home", "target_audience": "eco-conscious"},
        },
        {
            "content": "Luxury bedding made from organic cotton. Sleep better with premium materials.",
            "metadata": {"category": "home", "target_audience": "quality-seekers"},
        },
        {
            "content": "Home security systems with smart monitoring. Protect what matters most.",
            "metadata": {"category": "home", "target_audience": "security-minded"},
        },
        {
            "content": "Interior design consultations at affordable rates. Transform your space with expert help.",
            "metadata": {"category": "home", "target_audience": "design-enthusiasts"},
        },
        {
            "content": "Kitchen gadgets that make cooking faster and easier. Restaurant-quality meals at home.",
            "metadata": {"category": "home", "target_audience": "home-chefs"},
        },
        {
            "content": "Water filtration systems for cleaner, better-tasting water. Eco-friendly and cost-effective.",
            "metadata": {"category": "home", "target_audience": "health-conscious"},
        },
        # Automotive ads
        {
            "content": "Electric vehicles with industry-leading range. Go green without compromise.",
            "metadata": {"category": "automotive", "target_audience": "eco-drivers"},
        },
        {
            "content": "Luxury car leasing with all-inclusive maintenance. Drive a new model every two years.",
            "metadata": {
                "category": "automotive",
                "target_audience": "luxury-consumers",
            },
        },
        {
            "content": "Car insurance with rates based on your actual driving habits. Safe drivers save more.",
            "metadata": {"category": "automotive", "target_audience": "car-owners"},
        },
        {
            "content": "Off-road vehicle accessories for adventure enthusiasts. Tackle any terrain with confidence.",
            "metadata": {
                "category": "automotive",
                "target_audience": "outdoor-adventurers",
            },
        },
        {
            "content": "Professional auto detailing services that come to you. Showroom shine without leaving home.",
            "metadata": {
                "category": "automotive",
                "target_audience": "car-enthusiasts",
            },
        },
        {
            "content": "Affordable driving courses for new drivers. Build skills and confidence on the road.",
            "metadata": {"category": "automotive", "target_audience": "new-drivers"},
        },
        {
            "content": "High-performance tires for all weather conditions. Grip the road with confidence.",
            "metadata": {
                "category": "automotive",
                "target_audience": "safety-concerned",
            },
        },
        {
            "content": "Motorcycle gear designed for safety and style. Ride protected, look great.",
            "metadata": {"category": "automotive", "target_audience": "motorcyclists"},
        },
        # Pet ads
        {
            "content": "Premium pet food made with human-grade ingredients. Nutrition your pets deserve.",
            "metadata": {"category": "pets", "target_audience": "pet-owners"},
        },
        {
            "content": "Pet insurance that covers preventative care and emergencies. Peace of mind for pet parents.",
            "metadata": {"category": "pets", "target_audience": "devoted-pet-owners"},
        },
        {
            "content": "Interactive toys that keep pets engaged and active. Fight boredom while you're away.",
            "metadata": {"category": "pets", "target_audience": "busy-pet-owners"},
        },
        {
            "content": "Eco-friendly pet products made from sustainable materials. Better for pets and the planet.",
            "metadata": {
                "category": "pets",
                "target_audience": "eco-conscious-pet-owners",
            },
        },
    ]
