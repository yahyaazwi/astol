<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>نظام إدارة سائقي الوقود والشاحنات والطلبيات</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Cairo', sans-serif; /* تطبيق خط القاهرة على كامل الصفحة */
            background-color: #f5f7fa; /* لون خلفية الصفحة */
        }
        .tab-content {
            display: none; /* إخفاء محتوى التبويبات بشكل افتراضي */
        }
        .tab-content.active {
            display: block; /* إظهار محتوى التبويب النشط */
        }
        .card {
            transition: all 0.3s; /* تأثير انتقال سلس للبطاقات */
        }
        .card:hover {
            transform: translateY(-5px); /* رفع البطاقة قليلاً عند التحويم */
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1); /* إضافة ظل للبطاقة عند التحويم */
        }
        .stat-card {
            border-radius: 10px; /* زوايا دائرية لبطاقات الإحصائيات */
            padding: 20px; /* حشوة داخلية */
            color: white; /* لون النص أبيض */
            margin-bottom: 20px; /* هامش سفلي */
            position: relative; /* تموضع نسبي لإضافة أيقونة */
            overflow: hidden; /* إخفاء أي محتوى يتجاوز حدود البطاقة */
            cursor: pointer; /* إضافة مؤشر اليد للإشارة إلى أنه قابل للنقر */
        }
        .stat-card i {
            position: absolute; /* تموضع مطلق للأيقونة */
            left: 20px; /* المسافة من اليسار */
            bottom: 20px; /* المسافة من الأسفل */
            font-size: 3rem; /* حجم الأيقونة */
            opacity: 0.3; /* شفافية الأيقونة */
        }
        /* Custom styles for status colors from astol.html */
        .status-متاح { background-color: #a7f3d0; color: #065f46; } /* Green */
        .status-مشغول { background-color: #fde68a; color: #92400e; } /* Yellow */
        .status-غير-موجود { background-color: #fecaca; color: #991b1b; } /* Red */
        .status-صيانة { background-color: #bfdbfe; color: #1e40af; } /* Blue */
        .status-سائق-جديد { background-color: #e9d5ff; color: #6b21a8; } /* Purple */


        .modal-backdrop {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.5);
            z-index: 40; /* أقل من النافذة المنبثقة */
            display: none; /* مخفي بشكل افتراضي */
        }
        .modal {
            position: fixed;
            top: 50% ;
            left: 50% ;
            transform: translate(-50%, -50%);
            background-color: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
            z-index: 50; /* أعلى من الخلفية */
            width: 90%;
            max-width: 600px; /* تحديد عرض أقصى للنافذة */
            max-height: 90vh; /* تحديد ارتفاع أقصى للنافذة */
            overflow-y: auto; /* إضافة تمرير عمودي عند الحاجة */
            display: none; /* مخفي بشكل افتراضي */
            transition: opacity 0.25s ease;
        }
        .modal-active { /* يستخدم لإدارة حالة الفتح والإغلاق للجسم الرئيسي عند فتح النافذة */
            overflow-x: hidden;
            overflow-y: hidden !important; /* منع التمرير في الجسم الرئيسي عند فتح النافذة */
        }
        table {
            border-collapse: separate; /* فصل حدود خلايا الجدول */
            border-spacing: 0; /* بدون مسافات بين خلايا الجدول */
        }
        th, td {
            padding: 10px; /* حشوة داخلية لخلايا الجدول */
            vertical-align: middle; /* محاذاة عمودية للمحتوى في الوسط */
        }
        .map-container {
            height: 500px; /* ارتفاع حاوية الخريطة */
            background-color: #e9ecef; /* لون خلفية حاوية الخريطة */
            position: relative; /* تموضع نسبي لأيقونات الشاحنات والمحطات */
            border-radius: 0.5rem; /* زوايا دائرية */
        }
        .truck-icon {
            position: absolute; /* تموضع مطلق لأيقونات الشاحنات والمحطات */
            width: 30px; /* عرض الأيقونة */
            height: 30px; /* ارتفاع الأيقونة */
            background-color: #4299e1; /* لون خلفية الأيقونة */
            border-radius: 50%; /* جعل الأيقونة دائرية */
            display: flex; /* استخدام فليكس لمحاذاة المحتوى */
            align-items: center; /* محاذاة عمودية للمحتوى في الوسط */
            justify-content: center; /* محاذاة أفقية للمحتوى في الوسط */
            color: white; /* لون الأيقونة الداخلية أبيض */
            font-size: 12px; /* حجم الأيقونة الداخلية */
            box-shadow: 0 2px 4px rgba(0,0,0,0.2); /* ظل خفيف للأيقونة */
        }
        /* إعدادات الطباعة */
        @media print {
            .no-print {
                display: none !important;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px; /* Add some space above the table in print */
            }
            th, td {
                border: 1px solid #ddd;
                padding: 8px;
                text-align: right;
            }
            th {
                background-color: #f2f2f2;
            }
            /* Ensure status colors are visible in print if browser supports it */
            .status-متاح { background-color: #a7f3d0 !important; -webkit-print-color-adjust: exact; color: #065f46 !important; }
            .status-مشغول { background-color: #fde68a !important; -webkit-print-color-adjust: exact; color: #92400e !important; }
            .status-غير-موجود { background-color: #fecaca !important; -webkit-print-color-adjust: exact; color: #991b1b !important; }
            .status-صيانة { background-color: #bfdbfe !important; -webkit-print-color-adjust: exact; color: #1e40af !important; }
            .status-سائق-جديد { background-color: #e9d5ff !important; -webkit-print-color-adjust: exact; color: #6b21a8 !important; }

             /* Hide elements specific to the main view in print */
            .whatsapp-btn, .fa-image {
                display: none !important;
            }
        }
         /* Style for the image preview in the add/edit modal */
        #current-permit-image-preview {
            max-width: 100px;
            max-height: 100px;
            margin-top: 10px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        /* Style for the full image modal */
        #image-modal {
            background-color: rgba(0, 0, 0, 0.75); /* Dark overlay */
            z-index: 1000; /* Ensure it's on top */
        }

        #image-modal-content {
            max-width: 95%; /* Increased max width for better mobile view */
            max-height: 95%; /* Increased max height */
            overflow: auto; /* Add scroll if image is larger than modal */
            /* Removed fixed width/height to be more fluid */
        }

        #full-permit-image {
            display: block; /* Remove extra space below image */
            max-width: 100%; /* Image should fit within its container */
            max-height: 90vh; /* Limit image height to viewport height */
            margin: auto; /* Center the image */
        }

        /* Custom styles for the add/edit driver modal content */
        #driver-modal .modal-content {
            max-height: 80vh; /* Limit max height to 80% of viewport height */
            overflow-y: auto; /* Enable vertical scrolling if content exceeds max height */
        }

        /* Custom style for the WhatsApp icon button */
        .whatsapp-btn {
            display: inline-flex; /* Use flex to center icon and text */
            align-items: center; /* Center vertically */
            justify-content: center; /* Center horizontally */
            background-color: #25D366; /* WhatsApp green */
            color: white;
            padding: 6px 10px; /* Adjusted padding */
            border-radius: 8px; /* Rounded corners */
            text-decoration: none; /* Remove underline */
            font-size: 0.875rem; /* Small font size */
            font-weight: 500; /* Medium font weight */
            transition: background-color 0.2s ease-in-out; /* Smooth hover effect */
        }

        .whatsapp-btn:hover {
            background-color: #1EAD56; /* Darker green on hover */
        }

        .whatsapp-btn i {
            margin-left: 5px; /* Space between icon and text */
        }

        /* Style for print options modal */
        #print-options-modal .modal-content {
             max-height: 80vh;
             overflow-y: auto;
        }

        /* Style for clickable summary cards */
        .summary-card {
            cursor: pointer; /* Indicate it's clickable */
            user-select: none; /* Prevent text selection on click */
        }

        /* Style for editable table cells */
        .editable-cell {
            cursor: pointer;
            border-bottom: 1px dashed #ccc; /* Optional: Add a visual cue */
        }

         .editable-cell:hover {
            background-color: #f0f0f0; /* Optional: Highlight on hover */
         }

         .editable-cell input,
         .editable-cell select {
             width: 100%;
             padding: 0;
             margin: 0;
             border: none;
             background: none;
             outline: none;
         }

         .editable-cell input:focus,
         .editable-cell select:focus {
             outline: 1px solid #3b82f6; /* Highlight focus */
         }

         /* Style for delivery status indicator */
         .delivery-status-indicator {
             display: inline-block;
             width: 10px;
             height: 10px;
             border-radius: 50%;
             margin-left: 5px;
             vertical-align: middle;
         }

         .delivery-status-indicator.delivering {
             background-color: #f59e0b; /* Yellow/Orange */
             animation: pulse 1.5s infinite; /* Add pulse animation */
         }

         @keyframes pulse {
            0% {
                box-shadow: 0 0 0 0 rgba(245, 158, 11, 0.7);
            }
            70% {
                box-shadow: 0 0 0 10px rgba(245, 158, 11, 0);
            }
            100% {
                box-shadow: 0 0 0 0 rgba(245, 158, 11, 0);
            }
         }

    </style>
</head>
<body class="min-h-screen">
    <header class="bg-gradient-to-r from-blue-800 to-blue-600 text-white p-4 no-print">
        <div class="container mx-auto flex justify-between items-center">
            <div class="flex items-center">
                <i class="fas fa-truck-moving text-3xl mr-3 ml-2"></i>
                <h1 class="text-2xl font-bold">نظام إدارة سائقي الوقود والشاحنات والطلبيات</h1>
            </div>
            <div class="hidden lg:flex items-center space-x-4 space-x-reverse">
                <div class="relative">
                    <span class="absolute top-0 right-0 -mt-1 -mr-1 bg-red-500 text-white rounded-full w-5 h-5 flex items-center justify-center text-xs">3</span>
                    <i class="fas fa-bell text-xl cursor-pointer"></i>
                </div>
                <div class="flex items-center bg-blue-700 rounded-full p-1 pr-3">
                    <img src="https://placehold.co/40x40/7F9CF5/FFFFFF?text=User" alt="صورة المستخدم" class="w-8 h-8 rounded-full ml-2" onerror="this.onerror=null;this.src='https://placehold.co/40x40/EBF4FF/7F9CF5?text=Error';">
                    <span class="mr-2">مدير النظام</span>
                </div>
            </div>
        </div>
    </header>

    <div class="container mx-auto p-4">
        <div class="flex flex-wrap border-b border-gray-300 mb-4 no-print">
            <button class="px-4 py-2 text-blue-600 font-semibold border-b-2 border-blue-600 tab-btn active" data-tab="dashboard">
                <i class="fas fa-tachometer-alt ml-2"></i>لوحة التحكم
            </button>
            <button class="px-4 py-2 text-gray-600 font-semibold tab-btn" data-tab="drivers">
                <i class="fas fa-users ml-2"></i>السائقين
            </button>
            <button class="px-4 py-2 text-gray-600 font-semibold tab-btn" data-tab="trucks">
                <i class="fas fa-truck ml-2"></i>الشاحنات
            </button>
            <button class="px-4 py-2 text-gray-600 font-semibold tab-btn" data-tab="stations">
                <i class="fas fa-gas-pump ml-2"></i>محطات الوقود
            </button>
             <button class="px-4 py-2 text-gray-600 font-semibold tab-btn" data-tab="orders">
                <i class="fas fa-clipboard-list ml-2"></i>الطلبيات
            </button>
            <button class="px-4 py-2 text-gray-600 font-semibold tab-btn" data-tab="permits">
                <i class="fas fa-file-alt ml-2"></i>التصاريح
            </button>
            <button class="px-4 py-2 text-gray-600 font-semibold tab-btn" data-tab="tracking">
                <i class="fas fa-map-marker-alt ml-2"></i>تتبع الشاحنات
            </button>
            <button class="px-4 py-2 text-gray-600 font-semibold tab-btn" data-tab="reports">
                <i class="fas fa-chart-bar ml-2"></i>التقارير
            </button>
            <button class="px-4 py-2 text-gray-600 font-semibold tab-btn" data-tab="settings">
                <i class="fas fa-cog ml-2"></i>الإعدادات
            </button>
        </div>

        <div id="dashboard" class="tab-content active">
            <h2 class="text-2xl font-bold mb-6">لوحة التحكم</h2>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                <div class="stat-card bg-blue-600 card" data-tab="drivers">
                    <h3 class="text-lg font-semibold">عدد السائقين</h3>
                    <p class="text-3xl font-bold" id="totalDriversStat">0</p> <p class="text-sm opacity-75">+0% عن الشهر الماضي</p>
                    <i class="fas fa-user"></i>
                </div>

                <div class="stat-card bg-green-600 card">
                    <h3 class="text-lg font-semibold">عدد الشاحنات النشطة</h3>
                    <p class="text-3xl font-bold">132</p>
                    <p class="text-sm opacity-75">+5% عن الشهر الماضي</p>
                    <i class="fas fa-truck"></i>
                </div>

                <div class="stat-card bg-yellow-500 card">
                    <h3 class="text-lg font-semibold">عدد التصاريح السارية</h3>
                    <p class="text-3xl font-bold">98</p>
                    <p class="text-sm opacity-75">-2% عن الشهر الماضي</p>
                    <i class="fas fa-file-alt"></i>
                </div>

                <div class="stat-card bg-purple-600 card">
                    <h3 class="text-lg font-semibold">ملخص الطلبيات حسب الشركة</h3>
                     <div id="ordersSummaryStat" class="text-lg font-bold"></div>
                    <i class="fas fa-clipboard-list"></i>
                </div>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-8">
                <div class="bg-white rounded-lg shadow-md p-6 card">
                    <div class="flex justify-between items-center mb-4">
                        <h3 class="text-lg font-semibold">آخر عمليات التسليم</h3>
                        <button class="text-blue-600 hover:text-blue-800">عرض الكل</button>
                    </div>
                    <div class="overflow-x-auto">
                        <table class="w-full">
                            <thead>
                                <tr class="bg-gray-100">
                                    <th class="text-right py-2 px-3">#</th>
                                    <th class="text-right py-2 px-3">السائق</th>
                                    <th class="text-right py-2 px-3">المحطة</th>
                                    <th class="text-right py-2 px-3">الوقت</th>
                                    <th class="text-right py-2 px-3">الحالة</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr class="hover:bg-gray-50 border-b">
                                    <td class="py-2 px-3">1</td>
                                    <td class="py-2 px-3">عبدالباسط عبدالسلام</td>
                                    <td class="py-2 px-3">محطة الميدان</td>
                                    <td class="py-2 px-3">منذ 35 دقيقة</td>
                                    <td class="py-2 px-3"><span class="px-2 py-1 bg-green-100 text-green-800 rounded-full text-xs">مكتمل</span></td>
                                </tr>
                                <tr class="hover:bg-gray-50 border-b">
                                    <td class="py-2 px-3">2</td>
                                    <td class="py-2 px-3">جمعة مفتاح بوبكر</td>
                                    <td class="py-2 px-3">محطة القدس</td>
                                    <td class="py-2 px-3">منذ ساعة</td>
                                    <td class="py-2 px-3"><span class="px-2 py-1 bg-green-100 text-green-800 rounded-full text-xs">مكتمل</span></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <div class="bg-white rounded-lg shadow-md p-6 card">
                    <div class="flex justify-between items-center mb-4">
                        <h3 class="text-lg font-semibold">آخر التنبيهات</h3>
                        <button class="text-blue-600 hover:text-blue-800">عرض الكل</button>
                    </div>
                    <ul class="space-y-4">
                        <li class="flex items-start p-3 border-r-4 border-red-500 bg-red-50 rounded-md">
                            <div class="mr-4 ml-2 bg-red-500 rounded-full p-2 text-white">
                                <i class="fas fa-exclamation-triangle"></i>
                            </div>
                            <div>
                                <h4 class="font-semibold">تصريح منتهي الصلاحية</h4>
                                <p class="text-gray-600 text-sm">تصريح رقم 702125 للسائق ناصر ابراهيم منتهي الصلاحية منذ يومين</p>
                                <p class="text-gray-500 text-xs mt-1">منذ ساعة</p>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>

            <div class="mt-8 bg-white rounded-lg shadow-md p-6 card">
                <h3 class="text-lg font-semibold mb-4">أداء التسليم الشهري</h3>
                <div class="h-80 bg-gray-100 flex items-center justify-center rounded-md">
                    <p class="text-gray-500">الرسم البياني لأداء التسليم الشهري سيظهر هنا</p>
                </div>
            </div>
        </div>

        <div id="drivers" class="tab-content">
            <div class="bg-white p-4 sm:p-6 rounded-lg shadow-md mb-6 no-print">
                <h1 class="text-xl sm:text-2xl font-bold text-gray-800 mb-4">نظام إدارة سائقي نقل الوقود</h1>
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4 sm:gap-6 mb-6">
                    <div class="bg-green-500 text-white p-4 sm:p-5 rounded-xl shadow-lg flex items-center justify-between transform transition-transform hover:scale-105 summary-card" data-status="متاح">
                        <div>
                            <div id="total-available" class="text-2xl sm:text-3xl font-bold">0</div>
                            <div class="text-xs sm:text-sm">سائق متاح</div>
                        </div>
                        <i class="fas fa-check-circle text-green-200 text-3xl sm:text-4xl"></i>
                    </div>
                    <div class="bg-yellow-500 text-white p-4 sm:p-5 rounded-xl shadow-lg flex items-center justify-between transform transition-transform hover:scale-105 summary-card" data-status="مشغول">
                        <div>
                            <div id="total-busy" class="text-2xl sm:text-3xl font-bold">0</div>
                            <div class="text-xs sm:text-sm">سائق مشغول</div>
                        </div>
                        <i class="fas fa-clock text-yellow-200 text-3xl sm:text-4xl"></i>
                    </div>
                    <div class="bg-blue-500 text-white p-4 sm:p-5 rounded-xl shadow-lg flex items-center justify-between transform transition-transform hover:scale-105 summary-card" data-status="صيانة">
                        <div>
                            <div id="total-maintenance" class="text-2xl sm:text-3xl font-bold">0</div>
                            <div class="text-xs sm:text-sm">صيانة</div>
                        </div>
                        <i class="fas fa-tools text-blue-200 text-3xl sm:text-4xl"></i>
                    </div>
                    <div class="bg-red-500 text-white p-4 sm:p-5 rounded-xl shadow-lg flex items-center justify-between transform transition-transform hover:scale-105 summary-card" data-status="غير موجود">
                        <div>
                            <div id="total-absent" class="text-2xl sm:text-3xl font-bold">0</div>
                            <div class="text-xs sm:text-sm">غير موجود</div>
                        </div>
                        <i class="fas fa-times-circle text-red-200 text-3xl sm:text-4xl"></i>
                    </div>
                    <div class="bg-purple-500 text-white p-4 sm:p-5 rounded-xl shadow-lg flex items-center justify-between transform transition-transform hover:scale-105 summary-card" data-status="سائق جديد">
                        <div>
                            <div id="total-new" class="text-2xl sm:text-3xl font-bold">0</div>
                            <div class="text-xs sm:text-sm">سائق جديد</div>
                        </div>
                        <i class="fas fa-user-plus text-purple-200 text-3xl sm:text-4xl"></i>
                    </div>
                </div>

                <div class="flex flex-col md:flex-row items-center justify-between gap-4">
                    <input type="text" id="search-input" placeholder="بحث عن سائق..." class="w-full md:flex-grow p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500">
                    <div class="flex flex-wrap justify-center md:justify-end gap-4 w-full md:w-auto">
                        <button id="show-all-btn" class="bg-gray-300 text-gray-800 px-4 py-2 rounded-lg hover:bg-gray-400 focus:outline-none focus:ring-2 focus:ring-gray-300 focus:ring-opacity-50 w-full sm:w-auto hidden">
                            <i class="fas fa-list ml-2"></i> عرض كل السائقين
                        </button>
                        <button id="add-driver-btn" class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50 w-full sm:w-auto">
                            <i class="fas fa-user-plus ml-2"></i> إضافة سائق جديد
                        </button>
                        <button id="backup-btn" class="bg-yellow-500 text-white px-4 py-2 rounded-lg hover:bg-yellow-600 focus:outline-none focus:ring-2 focus:ring-yellow-500 focus:ring-opacity-50 w-full sm:w-auto">
                            <i class="fas fa-download ml-2"></i> نسخ احتياطي
                        </button>
                        <button id="print-options-btn" class="bg-gray-500 text-white px-4 py-2 rounded-lg hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-gray-500 focus:ring-opacity-50 w-full sm:w-auto">
                            <i class="fas fa-print ml-2"></i> خيارات الطباعة
                        </button>
                    </div>
                </div>
            </div>

            <div class="bg-white p-4 sm:p-6 rounded-lg shadow-md overflow-x-auto">
                <table id="drivers-table" class="min-w-full divide-y divide-gray-200">
                    <thead class="bg-gray-50">
                        <tr>
                            <th scope="col" class="px-3 py-2 sm:px-6 sm:py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                                الرقم التسلسلي
                            </th>
                            <th scope="col" class="px-3 py-2 sm:px-6 sm:py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                                الاسم
                            </th>
                            <th scope="col" class="px-3 py-2 sm:px-6 sm:py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                                رقم الهاتف
                            </th>
                            <th scope="col" class="px-3 py-2 sm:px-6 sm:py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider no-print">
                                واتساب
                            </th>
                            <th scope="col" class="px-3 py-2 sm:px-6 sm:py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                                رقم الشاحنة
                            </th>
                            <th scope="col" class="px-3 py-2 sm:px-6 sm:py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                                رقم المقطورة
                            </th>
                            <th scope="col" class="px-3 py-2 sm:px-6 sm:py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                                رقم التصريح
                            </th>
                            <th scope="col" class="px-3 py-2 sm:px-6 sm:py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                                حالة السائق
                            </th>
                            <th scope="col" class="px-3 py-2 sm:px-6 sm:py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                                آخر طلبية (المحطة والتاريخ)
                            </th>
                            <th scope="col" class="px-3 py-2 sm:px-6 sm:py-3 text-right text-sm font-medium text-gray-500 uppercase tracking-wider no-print">
                                إجراءات
                            </th>
                        </tr>
                    </thead>
                    <tbody id="drivers-table-body" class="bg-white divide-y divide-gray-200">
                        </tbody>
                </table>
            </div>

            <div id="driver-modal" class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full flex items-center justify-center hidden no-print p-4">
                <div class="bg-white p-6 sm:p-8 rounded-lg shadow-xl w-full max-w-sm sm:max-w-md modal-content">
                    <h2 id="modal-title" class="text-xl font-bold mb-4">إضافة سائق جديد</h2>
                    <form id="driver-form">
                        <input type="hidden" id="driver-id">
                        <div class="mb-4">
                            <label for="driver-name" class="block text-gray-700 text-sm font-bold mb-2">الاسم:</label>
                            <input type="text" id="driver-name" required class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                        </div>
                        <div class="mb-4">
                            <label for="driver-phone" class="block text-gray-700 text-sm font-bold mb-2">رقم الهاتف:</label>
                            <input type="tel" id="driver-phone" required class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                        </div>
                        <div class="mb-4">
                            <label for="driver-truck" class="block text-gray-700 text-sm font-bold mb-2">رقم الشاحنة:</label>
                            <input type="text" id="driver-truck" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                        </div>
                        <div class="mb-4">
                            <label for="driver-trailer" class="block text-gray-700 text-sm font-bold mb-2">رقم المقطورة:</label>
                            <input type="text" id="driver-trailer" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-shadow-outline">
                        </div>
                        <div class="mb-4">
                            <label for="driver-permit" class="block text-gray-700 text-sm font-bold mb-2">رقم التصريح:</label>
                            <input type="text" id="driver-permit" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                        </div>
                        <div class="mb-4">
                            <label for="driver-permit-image" class="block text-gray-700 text-sm font-bold mb-2">صورة التصريح (اختياري):</label>
                            <input type="file" id="driver-permit-image" accept="image/*" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                            <img id="current-permit-image-preview" src="" alt="صورة التصريح الحالية" class="hidden">
                        </div>
                        <div class="mb-4">
                            <label for="driver-status" class="block text-gray-700 text-sm font-bold mb-2">حالة السائق:</label>
                            <select id="driver-status" required class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                                <option value="متاح">متاح</option>
                                <option value="مشغول">مشغول</option>
                                <option value="غير موجود">غير موجود</option>
                                <option value="صيانة">صيانة</option>
                                <option value="سائق جديد">سائق جديد</option>
                            </select>
                        </div>
                        <div class="mb-4">
                            <label for="driver-last-delivery-station" class="block text-gray-700 text-sm font-bold mb-2">اسم محطة آخر طلبية:</label>
                            <input type="text" id="driver-last-delivery-station" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                        </div>
                        <div class="mb-4">
                            <label for="driver-last-delivery-date" class="block text-gray-700 text-sm font-bold mb-2">تاريخ آخر طلبية:</label>
                            <input type="date" id="driver-last-delivery-date" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                        </div>
                        <div class="flex items-center justify-between">
                            <div class="flex justify-between items-center mb-4">
    <button type="button" onclick="prevRow()" class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600">
        <i class="fas fa-arrow-right ml-2"></i>السابق
    </button>
    <span id="row-counter" class="text-gray-600"></span>
    <button type="button" onclick="nextRow()" class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600">
        التالي <i class="fas fa-arrow-left mr-2"></i>
    </button>
</div>
<button type="submit" id="submit-driver-btn" class="bg-green-500 text-white px-4 py-2 rounded-lg hover:bg-green-600 focus:outline-none focus:shadow-outline">إضافة</button>
                            <button type="button" id="close-modal-btn" class="bg-gray-500 text-white px-4 py-2 rounded-lg hover:bg-gray-600 focus:outline-none focus:shadow-outline">إلغاء</button>
                        </div>
                    </form>
                </div>
            </div>

            <div id="image-modal" class="fixed inset-0 bg-gray-600 bg-opacity-75 overflow-y-auto h-full w-full flex items-center justify-center hidden no-print p-4">
                <div id="image-modal-content" class="relative w-full max-w-lg lg:max-w-xl">
                    <button id="close-image-modal-btn" class="absolute top-0 right-0 mt-2 mr-2 text-white text-2xl font-bold z-10">&times;</button>
                    <img id="full-permit-image" src="" alt="صورة التصريح">
                </div>
            </div>

            <div id="print-options-modal" class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full flex items-center justify-center hidden no-print p-4">
                <div class="bg-white p-6 sm:p-8 rounded-lg shadow-xl w-full max-w-sm modal-content">
                    <h2 class="text-xl font-bold mb-4">خيارات الطباعة</h2>
                    <div class="mb-4">
                        <label class="inline-flex items-center">
                            <input type="radio" name="printScope" value="all" class="form-radio h-5 w-5 text-blue-600" checked>
                            <span class="ml-2 text-gray-700">طباعة الكشف كامل</span>
                        </label>
                    </div>
                    <div class="mb-4">
                        <label class="inline-flex items-center">
                            <input type="radio" name="printScope" value="متاح" class="form-radio h-5 w-5 text-green-600">
                            <span class="ml-2 text-gray-700">طباعة السائقين المتاحين فقط</span>
                        </label>
                    </div>
                    <div class="mb-4">
                        <label class="inline-flex items-center">
                            <input type="radio" name="printScope" value="مشغول" class="form-radio h-5 w-5 text-yellow-600">
                            <span class="ml-2 text-gray-700">طباعة السائقين المشغولين فقط</span>
                        </label>
                    </div>
                    <div class="mb-4">
                        <label class="inline-flex items-center">
                            <input type="radio" name="printScope" value="صيانة" class="form-radio h-5 w-5 text-blue-600">
                            <span class="ml-2 text-gray-700">طباعة السائقين في الصيانة فقط</span>
                        </label>
                    </div>
                    <div class="mb-4">
                        <label class="inline-flex items-center">
                            <input type="radio" name="printScope" value="غير موجود" class="form-radio h-5 w-5 text-red-600">
                            <span class="ml-2 text-gray-700">طباعة السائقين غير الموجودين فقط</span>
                        </label>
                    </div>
                    <div class="mb-4">
                        <label class="inline-flex items-center">
                            <input type="radio" name="printScope" value="سائق جديد" class="form-radio h-5 w-5 text-purple-600">
                            <span class="ml-2 text-gray-700">طباعة السائقين الجدد فقط</span>
                        </label>
                    </div>

                    <div class="flex items-center justify-between">
                        <button id="confirm-print-btn" class="bg-green-500 text-white px-4 py-2 rounded-lg hover:bg-green-600 focus:outline-none focus:shadow-outline">طباعة</button>
                        <button type="button" id="close-print-modal-btn" class="bg-gray-500 text-white px-4 py-2 rounded-lg hover:bg-gray-600 focus:outline-none focus:shadow-outline">إلغاء</button>
                    </div>
                </div>
            </div>
        </div>

        <div id="trucks" class="tab-content">
            <div class="flex justify-between items-center mb-6">
                <h2 class="text-2xl font-bold">إدارة الشاحنات والمقطورات</h2>
                <button class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md flex items-center shadow-md hover:shadow-lg transition-shadow">
                    <i class="fas fa-plus ml-2"></i> إضافة شاحنة جديدة
                </button>
            </div>
             <div class="bg-white p-4 rounded-lg shadow-md mb-6 card">
                <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <div>
                        <label for="truckSearchInput-trucks" class="block text-sm font-medium text-gray-700">بحث</label>
                        <div class="mt-1 relative rounded-md shadow-sm">
                            <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                                <i class="fas fa-search text-gray-400"></i>
                            </div>
                            <input type="text" id="truckSearchInput-trucks" class="focus:ring-blue-500 focus:border-blue-500 block w-full pr-10 sm:text-sm border-gray-300 rounded-md py-2" placeholder="رقم الشاحنة، الرقم الإشاري...">
                        </div>
                    </div>
                    <div>
                        <label for="truckStatusFilter-trucks" class="block text-sm font-medium text-gray-700">الحالة</label>
                        <select id="truckStatusFilter-trucks" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm py-2">
                            <option value="">الكل</option>
                            <option value="active">نشطة</option>
                            <option value="maintenance">في الصيانة</option>
                            <option value="inactive">غير نشطة</option>
                        </select>
                    </div>
                    <div>
                        <label for="truckCapacityFilter-trucks" class="block text-sm font-medium text-gray-700">سعة الحمولة</label>
                        <select id="truckCapacityFilter-trucks" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm py-2">
                            <option value="">الكل</option>
                            <option value="40000">40.000</option>
                            <option value="50000">50.000</option>
                            <option value="other">أخرى</option>
                        </select>
                    </div>
                </div>
            </div>
            <div class="bg-white rounded-lg shadow-md overflow-hidden card">
                <div class="overflow-x-auto">
                    <table class="min-w-full">
                        <thead class="bg-gray-50">
                            <tr class="bg-gray-100 text-gray-600 uppercase text-sm">
                                <th class="py-3 px-4 text-right">الرقم الإشاري</th>
                                <th class="py-3 px-4 text-right">رقم الشاحنة</th>
                                <th class="py-3 px-4 text-right">رقم المقطورة</th>
                                <th class="py-3 px-4 text-right">نوع الشاحنة</th>
                                <th class="py-3 px-4 text-right">سعة الحمولة</th>
                                <th class="py-3 px-4 text-right">تاريخ آخر صيانة</th>
                                <th class="py-3 px-4 text-right">اسم السائق الحالي</th>
                                <th class="py-3 px-4 text-right">الحالة</th>
                                <th class="py-3 px-4 text-right">إجراءات</th>
                            </tr>
                        </thead>
                        <tbody class="text-gray-700">
                            <tr class="border-b hover:bg-gray-50">
                                <td class="py-3 px-4">74</td>
                                <td class="py-3 px-4">1509</td>
                                <td class="py-3 px-4">1768</td>
                                <td class="py-3 px-4">شاحنة صهريج</td>
                                <td class="py-3 px-4">40.000</td>
                                <td class="py-3 px-4">15/05/2023</td>
                                <td class="py-3 px-4">عبدالباسط عبدالسلام</td>
                                <td class="py-3 px-4"><span class="bg-green-100 text-green-800 py-1 px-2 rounded-full text-xs">نشطة</span></td>
                                <td class="py-3 px-4">
                                    <div class="flex items-center space-x-3 space-x-reverse">
                                        <button class="text-blue-500 hover:text-blue-700" title="تعديل"><i class="fas fa-edit"></i></button>
                                        <button class="text-gray-500 hover:text-gray-700" title="سجل الصيانة"><i class="fas fa-history"></i></button>
                                        <button class="text-gray-500 hover:text-gray-700" title="عرض التفاصيل"><i class="fas fa-eye"></i></button>
                                    </div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

         <div id="stations" class="tab-content">
             <div class="flex justify-between items-center mb-6">
                <h2 class="text-2xl font-bold">إدارة محطات الوقود</h2>
                <button id="add-station-btn" class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md flex items-center shadow-md hover:shadow-lg transition-shadow">
                    <i class="fas fa-plus ml-2"></i> إضافة محطة جديدة
                </button>
            </div>

            <div id="station-modal" class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full flex items-center justify-center hidden no-print p-4">
                <div class="bg-white p-6 sm:p-8 rounded-lg shadow-xl w-full max-w-sm sm:max-w-md modal-content">
                    <h2 id="station-modal-title" class="text-xl font-bold mb-4">إضافة محطة جديدة</h2>
                    <form id="station-form">
                        <input type="hidden" id="station-id">
                         <div class="mb-4">
                            <label for="station-company" class="block text-gray-700 text-sm font-bold mb-2">الشركة:</label>
                            <select id="station-company" required class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                                 <option value="">اختر الشركة</option>
                                <option value="الشرارة">الشرارة</option>
                                <option value="الطرق السريعة">الطرق السريعة</option>
                                <option value="البريقة">البريقة</option>
                                <option value="ليبيا نفط">ليبيا نفط</option>
                            </select>
                        </div>
                        <div class="mb-4">
                            <label for="station-name" class="block text-gray-700 text-sm font-bold mb-2">اسم المحطة:</label>
                            <input type="text" id="station-name" required class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                        </div>
                         <div class="mb-4">
                            <label for="station-number" class="block text-gray-700 text-sm font-bold mb-2">رقم المحطة:</label>
                            <input type="text" id="station-number" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                        </div>
                         <div class="mb-4">
                            <label for="station-address" class="block text-gray-700 text-sm font-bold mb-2">العنوان (اختياري):</label>
                            <input type="text" id="station-address" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                        </div>
                        <div class="mb-4">
                            <label for="station-owner" class="block text-gray-700 text-sm font-bold mb-2">اسم صاحب المحطة:</label>
                            <input type="text" id="station-owner" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                        </div>
                        <div class="mb-4">
                            <label for="station-phone" class="block text-gray-700 text-sm font-bold mb-2">أرقام المحطة:</label>
                            <input type="tel" id="station-phone" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                        </div>
                        <div class="flex items-center justify-between">
                            <button type="submit" id="submit-station-btn" class="bg-green-500 text-white px-4 py-2 rounded-lg hover:bg-green-600 focus:outline-none focus:shadow-outline">إضافة</button>
                            <button type="button" id="close-station-modal-btn" class="bg-gray-500 text-white px-4 py-2 rounded-lg hover:bg-gray-600 focus:outline-none focus:shadow-outline">إلغاء</button>
                        </div>
                    </form>
                </div>
            </div>

             <div class="bg-white p-4 sm:p-6 rounded-lg shadow-md overflow-x-auto mt-6">
                <table id="stations-table" class="min-w-full divide-y divide-gray-200">
                    <thead class="bg-gray-50">
                        <tr>
                            <th scope="col" class="px-3 py-2 sm:px-6 sm:py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                                الرقم التسلسلي
                            </th>
                             <th scope="col" class="px-3 py-2 sm:px-6 sm:py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                                الشركة
                            </th>
                            <th scope="col" class="px-3 py-2 sm:px-6 sm:py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                                اسم المحطة
                            </th>
                             <th scope="col" class="px-3 py-2 sm:px-6 sm:py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                                رقم المحطة
                            </th>
                             <th scope="col" class="px-3 py-2 sm:px-6 sm:py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                                العنوان
                            </th>
                            <th scope="col" class="px-3 py-2 sm:px-6 sm:py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                                صاحب المحطة
                            </th>
                            <th scope="col" class="px-3 py-2 sm:px-6 sm:py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                                أرقام المحطة
                            </th>
                             <th scope="col" class="px-3 py-2 sm:px-6 sm:py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                                حالة التوصيل
                            </th>
                            <th scope="col" class="px-3 py-2 sm:px-6 sm:py-3 text-right text-sm font-medium text-gray-500 uppercase tracking-wider no-print">
                                إجراءات
                            </th>
                        </tr>
                    </thead>
                    <tbody id="stations-table-body" class="bg-white divide-y divide-gray-200">
                        </tbody>
                </table>
            </div>
        </div>

        <div id="orders" class="tab-content">
            <h2 class="text-2xl font-bold mb-6">إدارة الطلبيات</h2>

             <div class="bg-white p-4 sm:p-6 rounded-lg shadow-md mb-6 card">
                <h3 class="text-xl font-semibold mb-4">إضافة طلبية جديدة</h3>
                <form id="order-form" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    <div class="col-span-1">
                        <label for="order-warehouse" class="block text-gray-700 text-sm font-bold mb-2">المستودع:</label>
                        <select id="order-warehouse" required class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                            <option value="">اختر المستودع</option>
                            <option value="السرير">السرير</option>
                            <option value="راس المنقار">راس المنقار</option>
                        </select>
                    </div>
                    <div class="col-span-1">
                        <label for="order-company" class="block text-gray-700 text-sm font-bold mb-2">الشركة:</label>
                        <select id="order-company" required class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                             <option value="">اختر الشركة</option>
                            <option value="الشرارة">الشرارة</option>
                            <option value="الطرق السريعة">الطرق السريعة</option>
                            <option value="البريقة">البريقة</option>
                            <option value="ليبيا نفط">ليبيا نفط</option>
                        </select>
                    </div>
                     <div class="col-span-1">
                        <label for="order-notification-id" class="block text-gray-700 text-sm font-bold mb-2">رقم الإشعار:</label>
                        <input type="text" id="order-notification-id" required class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                    </div>
                    <div class="col-span-1">
                        <label for="order-date" class="block text-gray-700 text-sm font-bold mb-2">تاريخ الطلبية:</label>
                        <input type="date" id="order-date" required class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                    </div>
                     <div class="col-span-1">
                        <label for="order-fuel-type" class="block text-gray-700 text-sm font-bold mb-2">نوع الوقود:</label>
                        <select id="order-fuel-type" required class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                             <option value="">اختر نوع الوقود</option>
                            <option value="بنزين">بنزين</option>
                            <option value="ديزل">ديزل</option>
                        </select>
                    </div>
                    <div class="col-span-1">
                        <label for="order-quantity" class="block text-gray-700 text-sm font-bold mb-2">الكمية (لتر):</label>
                        <select id="order-quantity" required class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                            <option value="">اختر الكمية</option>
                            <option value="50000">50,000</option>
                            <option value="40000">40,000</option>
                            <option value="20000">20,000</option>
                            <option value="10000">10,000</option>
                        </select>
                    </div>
                     <div class="col-span-1">
                        <label for="order-station" class="block text-gray-700 text-sm font-bold mb-2">المحطة:</label>
                        <select id="order-station" required class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                             <option value="">اختر المحطة</option>
                             </select>
                    </div>
                    <div class="col-span-1">
                        <label for="order-driver" class="block text-gray-700 text-sm font-bold mb-2">السائق:</label>
                        <select id="order-driver" required class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                             <option value="">اختر السائق</option>
                             </select>
                    </div>
                    <div id="order-image-upload-container" class="col-span-full hidden">
                        <label class="block text-gray-700 text-sm font-bold mb-2">رفع صورة كشف الطلبيات:</label>
                        <div class="flex items-center justify-between">
                            <div class="relative">
                                <input type="file" id="order-image-upload" accept="image/*" class="hidden" onchange="previewOrderImage(this)">
                                <button type="button" onclick="document.getElementById('order-image-upload').click()" class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 focus:outline-none focus:shadow-outline">
                                    <i class="fas fa-upload ml-2"></i> اختر صورة
                                </button>
                                <span id="order-image-name" class="mr-2 text-sm text-gray-600">لم يتم اختيار صورة</span>
                            </div>
                            <button type="button" id="process-order-image" class="bg-purple-500 text-white px-4 py-2 rounded-lg hover:bg-purple-600 focus:outline-none focus:shadow-outline hidden">
                                <i class="fas fa-magic ml-2"></i> معالجة الصورة
                            </button>
                        </div>
                        <div class="mt-3">
                            <img id="order-image-preview" class="hidden max-w-xs rounded-lg shadow-md" alt="معاينة صورة الطلبية">
                        </div>
                        <div id="ocr-processing-status" class="mt-2 text-sm hidden">
                            <div class="flex items-center">
                                <i class="fas fa-spinner fa-spin ml-2"></i>
                                <span>جاري معالجة الصورة...</span>
                            </div>
                        </div>
                        <div id="ocr-result" class="mt-2 p-3 bg-gray-100 rounded-lg hidden">
                            <h4 class="font-bold mb-2">نتائج المعالجة:</h4>
                            <ul id="ocr-result-list" class="text-sm space-y-1"></ul>
                        </div>
                    </div>
                    <div class="col-span-full flex justify-end">
                         <button type="submit" class="bg-green-500 text-white px-4 py-2 rounded-lg hover:bg-green-600 focus:outline-none focus:shadow-outline">
                            <i class="fas fa-plus ml-2"></i> إضافة طلبية
                        </button>
                    </div>
                </form>
            </div>

             <div class="bg-white p-4 rounded-lg shadow-md mb-6 card">
                <label for="order-search-input" class="block text-sm font-medium text-gray-700">بحث في الطلبيات (اسم المحطة، رقم الإشعار، اسم السائق)</label>
                <div class="mt-1 relative rounded-md shadow-sm">
                    <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                        <i class="fas fa-search text-gray-400"></i>
                    </div>
                    <input type="text" id="order-search-input" class="focus:ring-blue-500 focus:border-blue-500 block w-full pr-10 sm:text-sm border-gray-300 rounded-md py-2" placeholder="بحث...">
                </div>
            </div>


            <div class="bg-white p-4 sm:p-6 rounded-lg shadow-md overflow-x-auto mt-6">
                <h3 class="text-xl font-semibold mb-4">قائمة الطلبيات</h3>
                 <table id="orders-table" class="min-w-full divide-y divide-gray-200">
                    <thead class="bg-gray-50">
                        <tr>
                            <th scope="col" class="px-3 py-2 sm:px-6 sm:py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                                #
                            </th>
                             <th scope="col" class="px-3 py-2 sm:px-6 sm:py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                                المستودع
                            </th>
                             <th scope="col" class="px-3 py-2 sm:px-6 sm:py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                                الشركة
                            </th>
                            <th scope="col" class="px-3 py-2 sm:px-6 sm:py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                                رقم الإشعار
                            </th>
                            <th scope="col" class="px-3 py-2 sm:px-6 sm:py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                                تاريخ الطلبية
                            </th>
                             <th scope="col" class="px-3 py-2 sm:px-6 sm:py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                                نوع الوقود
                            </th>
                            <th scope="col" class="px-3 py-2 sm:px-6 sm:py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                                الكمية (لتر)
                            </th>
                            <th scope="col" class="px-3 py-2 sm:px-6 sm:py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                                المحطة
                            </th>
                            <th scope="col" class="px-3 py-2 sm:px-6 sm:py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                                السائق
                            </th>
                            <th scope="col" class="px-3 py-2 sm:px-6 sm:py-3 text-right text-sm font-medium text-gray-500 uppercase tracking-wider no-print">
                                إجراءات
                            </th>
                        </tr>
                    </thead>
                    <tbody id="orders-table-body" class="bg-white divide-y divide-gray-200">
                        </tbody>
                </table>
            </div>
        </div>


        <div id="permits" class="tab-content">
            <div class="flex justify-between items-center mb-6">
                <h2 class="text-2xl font-bold">إدارة التصاريح</h2>
                <button class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-md flex items-center shadow-md hover:shadow-lg transition-shadow">
                    <i class="fas fa-plus ml-2"></i> إضافة تصريح جديد
                </button>
            </div>
        </div>
        <div id="tracking" class="tab-content">
            <div class="flex justify-between items-center mb-6">
                <h2 class="text-2xl font-bold">تتبع الشاحنات</h2>
                 <div class="map-container w-full rounded-lg shadow-md">
                    <div class="flex items-center justify-center h-full text-gray-500 text-lg">
                                             </div>
                     <div class="truck-icon" style="top: 50px; right: 100px;"><i class="fas fa-truck"></i></div>
                    <div class="truck-icon" style="top: 150px; right: 250px;"><i class="fas fa-truck"></i></div>
                     <div class="truck-icon" style="top: 250px; right: 50px;"><i class="fas fa-truck"></i></div>
                </div>
            </div>
        </div>
        <div id="reports" class="tab-content">
            <div class="flex justify-between items-center mb-6">
                <h2 class="text-2xl font-bold">التقارير والإحصائيات</h2>
            </div>
        </div>
        <div id="settings" class="tab-content">
            <div class="flex justify-between items-center mb-6">
                <h2 class="text-2xl font-bold">إعدادات النظام</h2>
            </div>
        </div>

    </div>

    <footer class="bg-gray-800 text-white p-6 mt-8 no-print">
        <div class="container mx-auto">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                <div>
                    <h3 class="text-xl font-bold mb-4">نظام إدارة سائقي الوقود والطلبيات</h3>
                    <p class="text-gray-400">نظام متكامل لإدارة أسطول الشاحنات ومحطات الوقود والسائقين والتصاريح والطلبيات.</p>
                </div>
                <div>
                    <h3 class="font-bold mb-4">روابط سريعة</h3>
                    <ul class="space-y-2">
                        <li><a href="#" class="text-gray-400 hover:text-white" onclick="showTab('dashboard'); return false;">الرئيسية</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white" onclick="showTab('drivers'); return false;">السائقين</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white" onclick="showTab('trucks'); return false;">الشاحنات</a></li>
                         <li><a href="#" class="text-gray-400 hover:text-white" onclick="showTab('stations'); return false;">محطات الوقود</a></li>
                         <li><a href="#" class="text-gray-400 hover:text-white" onclick="showTab('orders'); return false;">الطلبيات</a></li>
                    </ul>
                </div>
                <div>
                    <h3 class="font-bold mb-4">الدعم</h3>
                    <ul class="space-y-2">
                        <li><a href="#" class="text-gray-400 hover:text-white">المساعدة</a></li>
                        <li><a href="#" class="text-gray-400 hover:text-white">اتصل بنا</a></li>
                    </ul>
                </div>
                <div>
                    <h3 class="font-bold mb-4">تواصل معنا</h3>
                    <ul class="space-y-2">
                        <li class="flex items-center"><i class="fas fa-map-marker-alt ml-2"></i> طرابلس، ليبيا</li>
                        <li class="flex items-center"><i class="fas fa-phone ml-2"></i> 0911234567</li>
                    </ul>
                </div>
            </div>
            <div class="border-t border-gray-700 mt-8 pt-6 text-center text-gray-400">
                <p>&copy; <span id="currentYear"></span> نظام إدارة سائقي الوقود والشاحنات والطلبيات. جميع الحقوق محفوظة.</p>
            </div>
        </div>
    </footer>


    <script>
    // كود للتعامل مع رفع صورة كشف الطلبيات والتعرف على النصوص العربية
    document.addEventListener('DOMContentLoaded', function() {
        // عرض/إخفاء حقل رفع الصورة بناءً على اختيار الشركة
        const companySelect = document.getElementById('order-company');
        const imageUploadContainer = document.getElementById('order-image-upload-container');
        
        if (companySelect && imageUploadContainer) {
            companySelect.addEventListener('change', function() {
                // إظهار حقل رفع الصورة فقط إذا كانت الشركة هي الشرارة
                if (this.value === 'الشرارة') {
                    imageUploadContainer.classList.remove('hidden');
                } else {
                    imageUploadContainer.classList.add('hidden');
                    // إعادة تعيين حقل الصورة
                    resetImageUpload();
                }
            });
        }
        
        // زر معالجة الصورة
        const processImageBtn = document.getElementById('process-order-image');
        if (processImageBtn) {
            processImageBtn.addEventListener('click', processOrderImage);
        }
    });
    
    // عرض معاينة الصورة المختارة
    function previewOrderImage(input) {
        const preview = document.getElementById('order-image-preview');
        const imageName = document.getElementById('order-image-name');
        const processBtn = document.getElementById('process-order-image');
        
        if (input.files && input.files[0]) {
            const fileName = input.files[0].name;
            imageName.textContent = fileName;
            
            const reader = new FileReader();
            reader.onload = function(e) {
                preview.src = e.target.result;
                preview.classList.remove('hidden');
                processBtn.classList.remove('hidden');
            };
            reader.readAsDataURL(input.files[0]);
        } else {
            resetImageUpload();
        }
    }
    
    // إعادة تعيين حقل رفع الصورة
    function resetImageUpload() {
        const preview = document.getElementById('order-image-preview');
        const imageName = document.getElementById('order-image-name');
        const processBtn = document.getElementById('process-order-image');
        const uploadInput = document.getElementById('order-image-upload');
        const ocrResult = document.getElementById('ocr-result');
        const ocrStatus = document.getElementById('ocr-processing-status');
        
        if (uploadInput) uploadInput.value = '';
        if (preview) preview.classList.add('hidden');
        if (imageName) imageName.textContent = 'لم يتم اختيار صورة';
        if (processBtn) processBtn.classList.add('hidden');
        if (ocrResult) ocrResult.classList.add('hidden');
        if (ocrStatus) ocrStatus.classList.add('hidden');
    }
    
    // معالجة صورة كشف الطلبيات باستخدام OCR
    function processOrderImage() {
        const ocrStatus = document.getElementById('ocr-processing-status');
        const ocrResult = document.getElementById('ocr-result');
        const ocrResultList = document.getElementById('ocr-result-list');
        
        // إظهار حالة المعالجة
        ocrStatus.classList.remove('hidden');
        ocrResult.classList.add('hidden');
        
        // محاكاة عملية معالجة OCR (في التطبيق الحقيقي، سيتم استدعاء خدمة OCR)
        setTimeout(function() {
            // إخفاء حالة المعالجة
            ocrStatus.classList.add('hidden');
            
            // بيانات وهمية للتوضيح (في التطبيق الحقيقي، ستأتي من خدمة OCR)
            const extractedData = {
                notificationId: 'SH-' + Math.floor(Math.random() * 10000),
                date: new Date().toISOString().split('T')[0],
                fuelType: Math.random() > 0.5 ? 'بنزين' : 'ديزل',
                quantity: [10000, 20000, 40000, 50000][Math.floor(Math.random() * 4)],
                station: 'محطة الميدان'
            };
            
            // عرض البيانات المستخرجة
            ocrResultList.innerHTML = '';
            for (const [key, value] of Object.entries(extractedData)) {
                const li = document.createElement('li');
                let label = '';
                
                switch(key) {
                    case 'notificationId': label = 'رقم الإشعار'; break;
                    case 'date': label = 'تاريخ الطلبية'; break;
                    case 'fuelType': label = 'نوع الوقود'; break;
                    case 'quantity': label = 'الكمية'; break;
                    case 'station': label = 'المحطة'; break;
                }
                
                li.innerHTML = `<span class="font-semibold">${label}:</span> ${value}`;
                ocrResultList.appendChild(li);
            }
            
            // إظهار نتائج المعالجة
            ocrResult.classList.remove('hidden');
            
            // ملء النموذج بالبيانات المستخرجة
            fillOrderForm(extractedData);
            
        }, 2000); // محاكاة تأخير المعالجة
    }
    
    // ملء نموذج الطلبية بالبيانات المستخرجة من الصورة
    function fillOrderForm(data) {
        // ملء حقول النموذج
        if (data.notificationId) {
            document.getElementById('order-notification-id').value = data.notificationId;
        }
        
        if (data.date) {
            document.getElementById('order-date').value = data.date;
        }
        
        if (data.fuelType) {
            const fuelTypeSelect = document.getElementById('order-fuel-type');
            for (let i = 0; i < fuelTypeSelect.options.length; i++) {
                if (fuelTypeSelect.options[i].value === data.fuelType) {
                    fuelTypeSelect.selectedIndex = i;
                    break;
                }
            }
        }
        
        if (data.quantity) {
            const quantitySelect = document.getElementById('order-quantity');
            for (let i = 0; i < quantitySelect.options.length; i++) {
                if (quantitySelect.options[i].value == data.quantity) {
                    quantitySelect.selectedIndex = i;
                    break;
                }
            }
        }
        
        // تحديث قائمة المحطات (في التطبيق الحقيقي، قد تحتاج إلى استدعاء API)
        if (data.station) {
            const stationSelect = document.getElementById('order-station');
            // إضافة المحطة المستخرجة إذا لم تكن موجودة
            let stationExists = false;
            for (let i = 0; i < stationSelect.options.length; i++) {
                if (stationSelect.options[i].value === data.station) {
                    stationSelect.selectedIndex = i;
                    stationExists = true;
                    break;
                }
            }
            
            if (!stationExists && data.station) {
                const option = document.createElement('option');
                option.value = data.station;
                option.textContent = data.station;
                stationSelect.appendChild(option);
                stationSelect.value = data.station;
            }
        }
    }
</script>
<script>
        // Tab Switching
        const tabBtns = document.querySelectorAll('.tab-btn');
        const tabContents = document.querySelectorAll('.tab-content');

        function showTab(tabId) {
            tabBtns.forEach(b => {
                b.classList.remove('active', 'border-blue-600', 'text-blue-600');
                b.classList.add('text-gray-600');
            });
            tabContents.forEach(content => {
                content.classList.remove('active');
            });

            const btnToShow = document.querySelector(`.tab-btn[data-tab="${tabId}"]`);
            const contentToShow = document.getElementById(tabId);

            if (btnToShow) {
                btnToShow.classList.add('active', 'border-blue-600', 'text-blue-600');
                btnToShow.classList.remove('text-gray-600');
            }
            if (contentToShow) {
                contentToShow.classList.add('active');
                // If the drivers tab is activated, ensure the table is rendered and summaries are updated
                if (tabId === 'drivers') {
                     loadDrivers(); // Ensure drivers are loaded
                     renderDrivers(searchInput.value); // Render the drivers table with current search term
                     updateDriversSummaries(); // Update summary counts
                } else if (tabId === 'stations') {
                     loadStations(); // Ensure stations are loaded
                     loadOrders(); // Ensure orders are loaded to check delivery status
                     renderStations(); // Render the stations table
                } else if (tabId === 'orders') {
                     loadStations(); // Ensure stations are loaded for dropdown
                     loadDrivers(); // Ensure drivers are loaded for dropdown
                     loadOrders(); // Ensure orders are loaded for table
                     renderOrders(orderSearchInput.value); // Render the orders table with current search filter
                     populateOrderFormDropdowns(); // Populate dropdowns in order form
                } else if (tabId === 'dashboard') {
                    loadOrders(); // Ensure orders are loaded for the summary
                    loadStations(); // Ensure stations are loaded to get company names
                    updateOrdersSummary(); // Update the orders summary on the dashboard
                }
            }
            window.scrollTo(0, 0);
        }

        tabBtns.forEach(btn => {
            btn.addEventListener('click', (event) => {
                const tabId = event.currentTarget.getAttribute('data-tab');
                showTab(tabId);
            });
        });

        // --- Start of Existing JavaScript from astol.html (for Drivers) ---

        // Key for localStorage for Drivers
        const DRIVERS_LOCAL_STORAGE_KEY = 'fuelDriversData';

        // Array to hold driver data
        let drivers = [];

        // Get table body element for Drivers
        const driversTableBody = document.getElementById('drivers-table-body');
        const driversTable = document.getElementById('drivers-table'); // Get the main table element
        // Get summary elements for Drivers
        const totalAvailableEl = document.getElementById('total-available');
        const totalBusyEl = document.getElementById('total-busy');
        const totalMaintenanceEl = document.getElementById('total-maintenance');
        const totalAbsentEl = document.getElementById('total-absent');
        const totalNewEl = document.getElementById('total-new');

         // Get summary card divs for Drivers
        const summaryCards = document.querySelectorAll('.summary-card');


        // Get add/edit modal elements for Drivers
        const driverModal = document.getElementById('driver-modal');
        const modalTitleEl = document.getElementById('modal-title');
        const addDriverBtn = document.getElementById('add-driver-btn');
        const closeModalBtn = document.getElementById('close-modal-btn');
        const driverForm = document.getElementById('driver-form');
        // وظائف التنقل بين الصفوف
let currentRowIndex = 0;
let rowsData = [];

function populateForm(rowIndex) {
    const row = rowsData[rowIndex];
    document.getElementById('driver-name').value = row.name || '';
    document.getElementById('driver-phone').value = row.phone || '';
    document.getElementById('driver-truck').value = row.truck || '';
    document.getElementById('driver-trailer').value = row.trailer || '';
}

function nextRow() {
    if (currentRowIndex < rowsData.length - 1) {
        currentRowIndex++;
        populateForm(currentRowIndex);
        updateCounter();
    }
}

function prevRow() {
    if (currentRowIndex > 0) {
        currentRowIndex--;
        populateForm(currentRowIndex);
        updateCounter();
    }
}

function updateCounter() {
    document.getElementById('row-counter').textContent = `الصف ${currentRowIndex + 1} من ${rowsData.length}`;
}

function initRows() {
    const rows = document.querySelectorAll('#drivers-table-body tr');
    rowsData = Array.from(rows).map(row => ({
        name: row.cells[0].textContent,
        phone: row.cells[1].textContent,
        truck: row.cells[2].textContent,
        trailer: row.cells[3].textContent
    }));
    
    if (rowsData.length > 0) {
        populateForm(0);
        updateCounter();
    }
}

// تهيئة البيانات عند تحميل الصفحة
window.addEventListener('DOMContentLoaded', initRows);

const submitDriverBtn = document.getElementById('submit-driver-btn');
        const driverIdInput = document.getElementById('driver-id');
        // Get form inputs for Drivers
        const driverNameInput = document.getElementById('driver-name');
        const driverPhoneInput = document.getElementById('driver-phone');
        const driverTruckInput = document.getElementById('driver-truck');
        const driverTrailerInput = document.getElementById('driver-trailer');
        const driverPermitInput = document.getElementById('driver-permit');
        const driverPermitImageInput = document.getElementById('driver-permit-image');
        const currentPermitImagePreview = document.getElementById('current-permit-image-preview');
        const driverStatusInput = document.getElementById('driver-status');
        const driverLastDeliveryStationInput = document.getElementById('driver-last-delivery-station');
        const driverLastDeliveryDateInput = document.getElementById('driver-last-delivery-date');

        // Get image modal elements
        const imageModal = document.getElementById('image-modal');
        const fullPermitImage = document.getElementById('full-permit-image');
        const closeImageModalBtn = document.getElementById('close-image-modal-btn');

        // Get print options modal elements
        const printOptionsModal = document.getElementById('print-options-modal');
        const printOptionsBtn = document.getElementById('print-options-btn'); // Changed from printBtn
        const closePrintModalBtn = document.getElementById('close-print-modal-btn');
        const confirmPrintBtn = document.getElementById('confirm-print-btn');
        const printScopeRadios = document.querySelectorAll('input[name="printScope"]');


        // Get search input for Drivers
        const searchInput = document.getElementById('search-input');
        // Get backup button for Drivers
        const backupBtn = document.getElementById('backup-btn');
        // Get Show All button for Drivers
        const showAllBtn = document.getElementById('show-all-btn');

        // Variable to store the raw text content from the uploaded document (for initial load)
        const uploadedDocumentContent = `اسم السائق,,رقم الشاحنة,رقم المقطورة,رقم التصريح التعبئة,الحمولة,رقم الهاتف,الرقم ,الاشاري,للشاحنة
عبدالباسط عبدالسلام ,1509 ,1768 ,6640 , 40.000,0914460103,0924460103 ,74
جمعة مفتاح بوبكر,12,4380,700792,50.000,0924315640,75
احمد صالح ذاوود,101,2021!,702175,50.000,0923180251,76
صالح يوسف صالح,13569-8,189-301,701111,50.000,0923116218,77
رمزي بوبكر عبدالحميد,14422,325!,702099,40.000,0917306493,0924065110,78
 محمد حسين محمد , 12053, 9154!,50, 50.000, 0924133186,79
احمد حسين عبدالرازق,8585,94,700328,50.000,0924739265,0913798652,80

كشف رقم (1)

اسم السائق,, ,رقم الشاحنة,رقم المقطورة,رقم التصريح التعبئة,الحمولة,رقم الهاتف,الرقم,الاشاري للشاحنة
ابوبكر محمد ابوبكر ,1662,2913,702053,50.000, ,67
 فتح الله محمد حمد, 40825-5, 31772-5, 701595,50.000,0924472004,0917807335,68
قريرة صلاح محمد,917-30,7603-8,701321 ,50.000,0925332824 ,69
احمد محمد ابوبكر,1845,3174,702057!,50.000,0915574456,0925574456,70
محمد سعد جابر , , ,13796 , , ,71
محمد علي بشير , 3374-8,34753-5 , 701739,40.000 ,0925783118 ,72
خالد علي بشير  ,7179-25-6,4150-8-2 , 701442, 40.000,0926426249,0918581605 ,73

كشف رقم
(2)

اسم السائق,,,رقم الشاحنة,رقم المقطورة,رقم التصريح التعبئة,الحمولة,رقم الهاتف,الرقم,الاشاري للشاحنة
عمر فرج علي  ,751,1735,701181,40.000,0945068894,60
صلاح فرج حمد محمد,46328,33941,702004,50.000,0917509226,61
عبدالله مختار عبدالله,2039-14,1220-30,700760,40.000,0926741129,63
علي مفتاح علي,1392-30,3732-25,701901,50.000,0924034128,64
عبد السلام عبد الجواد عبد السلام, , ,23166 , , ,65
سند سالم سعد,7606,1128,701046,50.000,0944046344,66

كشف رقم ( 3 )

اسم السائق,,,رقم الشاحنة,رقم المقطورة,رقم التصريح التعبئة,الحمولة,رقم الهاتف,الرقم الاشاري للشاحنة
ناصر ابراهيم,1074,2900,702125,40.000,0922223422,0911761004,59
فرجاني بوعجيلة عبدالغني,82704,#########,,20.000,,58
عبدالسلام ونيس محمد,!,6237,701321,50.000,0916297463,145
 اجويلي فتحي اجويلي,12810-5,20683-5,,,0917050113,146
مهدي محمد مفتاح ,575-12,9255,!,,0926943566,حاليا الاسكندرية,147
بالعيد يوسف مفتاح ,2125,12219,!,,0923897192,148
ادريس جاب الله ,17081 ,33886 , ,50.000,,149

كشف رقم ( 4 )

اسم السائق,,,رقم الشاحنة,رقم المقطورة,رقم التصريح التعبئة,الحمولة,رقم الهاتف,الرقم ,الاشاري,للشاحنة
محمد فضل الله سليمان,13434,13066,700373,40.000,0925255308,51
المهدي محمد عوض , , , 07387, , ,52
سعيد يوسف سعيد  ,13050 ,34248  , , !40.000, 0922934053,53
وائل جبريل حمد , 1033,8200 , , ,0922932252,54
احمد عبدالله علي,13404,12367,701500,40.000,0928401287,55
اسلام عمر محمد , , ,11174 , , ,56
اشرف حسين محمد    ,2317 ,4047 , ,40.000 ,0925545347,0917398410,57

كشف رقم ( 5)

اسم السائق,,,رقم الشاحنة,رقم المقطورة,رقم التصريح التعبئة,الحمولة,رقم الهاتف,الرقم الاشاري ,للشاحنة
زيدان عبد الكريم حسن ,  ,  ,13528 , ,  ,44
اشرف عبد الحميد علي , , ,02480 , , ,45
خالد فضل الله , 8019,18856 , , 50.000, ,47
مهند جمعة الدوكالي ,2153,17865,702174,50.000,0921202116,0911202116,48
محمود رمضان خليفة ,8969-5,34369-5,700267,40.000,0915932125,0918957328,49
فتحي عبدالرحيم يونس,72/35,1927,701904,40.000,0924006962,50

كشف رقم  ( 6) /

اسم السائق,,,رقم الشاحنة,رقم المقطورة,رقم التصريح التعبئة,الحمولة,رقم الهاتف,الرقم الاشاري ,للشاحنة
حسن سالم حمد ,49014-5 ,31285-3,701323,,40.000,0928852268,37
عادل علي قضوار,12380,8939,701327,50.000,0925496990,38
أسامة محمد جابر,66-84,30-4094,701604,50.000,0913269480,39
علي حسين شعيب ,	 , , ,50 ,0921000195 ,40
 مجدي جمعة محمد,46160-5 ,27110-5 ,702218, 40.000,0917177814, 0945089136,صيانة,41
 بدر رجب عبدالعزيز , 13844-8, 13500-8,702349 , , 0921000842,42
سالم محمد عبدالله,1785-30,1897-30,701989,40.000,0923579878,43

كشف رقم ( 7)

اسـم الــســائــق,,,رقــم الــشـاحـنـة,رقــــم الــمــقطورة,رقم التصريح التعبئة,الحمولة,رقم الهاتف,الرقم,الاشاري,للشاحنة
حمدي عبدالله موسي,13199-8,12862-8,702159,40.000,0923729124,30
فرج عبدالنبي سليمان,135-52,33448-5,701740,50.000,0926073348,0926073343,31
عبدالله فرج السنوسي ,1081,35257,702189!,50.000,0911921092,32
حمزة علي حسن,996,1745,701678!,50.000,0915552807,33
علي المختار علي,11826,16350,701468!,40.000,0925238032,صيانة ,34
ابوبكر صالح ابوبكر , , ,21913, , ,35
عصام رجب سالم ,  , ,24610 , , ,36

كشف رقم ( 8 )

اسم السائق,,,رقم الشاحنة,رقم المقطورة,رقم التصريح التعبئة,الحمولة,رقم الهاتف,الرقم الاشاري,للشاحنة
 مفتاح حمد صالح , 12194, 2915,! , ,0922932252 , يوم17/4,صيانة 3 ايام
 نوري حسن محمد  ,7666-8,12883-8,702171,50.000, 0945957217,0915734552,24
سليمان محمد علي ,17461-5,24917-5, ,40.000,0914038334,صيانة حاليا
خالد خميس مسعود,1383-30,2404-30,702191,50.000,0911667275,26
احمد صالح يونس,1937,10341,!,,0915265287,27
حسن سليمان عثمان,33780,10466,700232!,50.000,0926431509,28
عادل حسين علي  , 13909-8, 13037-25, 702356, 50.000,0923155854 ,29 !

كشف رقم ( 9 )

اسم السائق,,,رقم الشاحنة,رقم المقطورة,رقم التصريح التعبئة,الحمولة,رقم الهاتف,الرقم,الاشاري للشاحنة
جبريل امهنى عبدالرحمن ,47569-5 ,9148-8 , !,50.000, 0923202014,16
يونس صالح يونس,13105-8,13584-8,700839,50.000,0930873758,0911897502,17
جبريل امهنى عبدالرحمن ,47569-5 ,9148-8 , !,50.000, 0923202014,18
عطية فظل الله , 7791-8, 27668-5, ,40.000 , 0915124977,19
خير الله عبد الهادي خير الله,10767,2503,700881!,40.000,,20
خير الله سليمان داوود,73-5,36511,702205!,40.000,0916902532,21
عبدالباسط صالح سليمان  , 2126,702206 , 70, 50.000,0913965115,0916902532 ,22

كشف رقم (10 )
كشف رقم

اسم السائق,,,رقم الشاحنة,رقم المقطورة,رقم التصريح التعبئة,الحمولة,رقم الهاتف,الرقم ,الاشاري,للشاحنة
 عبدالسلام عبدالحميد, 49191, 38582, 702364!, 50.000, 0928156265,9
أسامة أنويجي مفتاح  , 12707, 1938, ,40.000,0925594085,10
محمد السنوسي الطالب  , , ,23165 , , ,11
خالد صالح خالد ,10116-8,1070-14,700846,40.000,0927891712,12
احمد عطية سليمان,499,1685,700873,50.000,0927282044,13
عادل حسين علي  ,13909 ,13037 , ,50.000 ,0923155854 ,14
امبارك فرج  , 6622,7772 ,	!	 ,50.000 ,0928017868,15

(11 )
كشف رقم

اسم السائق,,,رقم الشاحنة,رقم المقطورة,رقم التصريح التعبئة,الحمولة,رقم الهاتف,الرقم ,الاشاري,للشاحنة
عزام علي  ,18074 ,6923 , ,50.000, 0910447882,1
عبد الروؤف محمد,13536,13074,702130,50.000,0916202608,2
أكرم سعيد,35121,4980,700966,50.000,0917285964,3
حاتم سالم الناجي,2426-30,10165-8,702041,50.000,0918572006,4
معتز عبدالعزيز صالح ,86-52,96-52,,40,0913021206,5
فرج جبريل محمود,9129,27294,701763!,40.000,0915887322,6
ونيس عمر محمد,4895,6713,700251!,40.000,0944601885,7
   علي احسين شعيب ,38146 ,13818 , !,50.000 ,0921000195,8

(12 )
كشف رقم

اسم السائق,,,رقم الشاحنة,رقم المقطورة,رقم التصريح التعبئة,الحمولة,رقم الهاتف,الرقم ,الاشاري,للشاحنة
عبدالباسط فرج جبريل , 11017, 12945, ,50.000,0914137021,81
,,,,,,82
ارجيه سعد عبدالنبي  ,36106 ,6587 ,! ,50.000 ,0919368121 ,83
حماد ناصف بوبكر  ,1527-14 ,981-14 ,700151,50.000 ,0913964050 ,84
محمد حسين سعد,13576,32715,,50.000,0915725023,85
اجويلي موسي اجويلي ,9308 ,36937 , ,50.000,0926915062 ,86
سليمان ناجي محمد  ,9166 ,3684 , ,50.000 ,0914595907 ,87
امحمد سالم الكوشي  ,  7626-8, 488-36, !, , 0915104518,88

(   13 )
كشف رقم

اسم السائق,,,رقم الشاحنة,رقم المقطورة,رقم التصريح التعبئة,الحمولة,رقم الهاتف,الرقم ,الاشاري,للشاحنة
حسام محمد عامر  ,5520 ,2492 ,701637 ,,0914594931,89
الصغير علي الصغير ,  , , 21646,, ,90
عادل عبدالفتاح عبدالله  ,1132-6 ,10436-8 , ,50,0914460702,91
 حسين جادالله سليمان ,39692-5 ,33794-5 ,700639,50 , 0931916312,92
محمد حماد ناصف ,1671-30,8927-8,702072,40.000,0926072248,93
حماد عبد القادر عبد الهادي , , ,21640 , , ,94
عادل مفتاح حسين  ,13376 ,13165 ,702184 ,! , 0913498290,95
جمعه ونيس حمد , , ,20517, , ,96

(  14  )
كشف رقم

اسم السائق,,,رقم الشاحنة,رقم المقطورة,رقم التصريح التعبئة,الحمولة,رقم الهاتف,الرقم ,الاشاري,للشاحنة
احمد فرج الشكري  ,13691 , 6794, ,40.000,0915481819,97
خالد فرج عبدالسلام  , 2333,3833 , ,40.000,0925119886,98
موسى حسن مصباح ,  , ,24275 , , ,99
محمد ادم عبدالكريم, 5439,8909 ,700503, , 0920958139,100
 حمزه ادريس حمد, 8158-8, 638-14,!,40.000,0920958139,101
 حافظ عبدالكريم,  , , !,50.000,0917525072 ,102
فتحي علي مفتاح  ,13034-8,32631-5 ,702017 , 50.000, 0913748859,103
محمد مفتاح مفتاح , , ,02542, , ,104

(  15  )
كشف رقم

اسم السائق,,,رقم الشاحنة,رقم المقطورة,رقم التصريح التعبئة,الحمولة,رقم الهاتف,الرقم الاشاري ,للشاحنة
 محمد مفتاح مفتاح ,3791,14456,! ,50.000,0918883798,0921183798,105
اسلام عمر محمد ,  ,  ,11174 , , ,106
حسن سالم حمد , , , 07937, , ,107
محمد السنوسي الطالب , , ,23165, , ,108
عصام رجب سالم , , ,24610,, ,109
احمد ابريك عبد الحميد ,, ,18681 ,, ,110
   طارق محمد بوبكر  , , , , , ,111
حامد موسى محمد  ,8702-8 ,9024-8 , ,50 , 0926224658,112

( 16   )
كشف رقم

اسم السائق,,,رقم الشاحنة,رقم المقطورة,رقم التصريح التعبئة,الحمولة,رقم الهاتف,الرقم ,الاشاري,للشاحنة
عبدالكريم محمد الزروق ,13635 ,2584 , ,50,0917621407,113
 عبدالمولي عبدالسلام,     26  ,21 , ,,0924985221,114
محمد سعيد فتح الله ,508-2 ,4980-3 , 702291, , 0931809277,115
سالم عبدالكريم محمد  , 7759,18149 , ,50.000 , 0924507372,116
مسعود عبدالحفيظ مسعود,1111-12,24764-5,701649, 50.000,0917381707,117
موسي عبدالكريم حمد ,858-12 ,878-12 ,700549 ,40.000,0916728545 ,118 !
موسى فرج موسي ,13115 ,2978 , , 50.000,   0927354920,119
محمد ناجي ,18,1663,,50.000,0926418744,120

(  17  )
سكشف رقم

اسم السائق,,,رقم الشاحنة,رقم المقطورة,رقم التصريح التعبئة,الحمولة,رقم الهاتف,الرقم ,الاشاري,للشاحنة
سالم الزوام مصطفى ,972 ,14526 ,! ,,0924306305,121
عامر محمد عامر , 158,158 , !,40.000 ,0928475376,122
احمد محمود محمد ,2242-30 ,3980-30 ,702297 , , 0918023025,123
محمد فرج جبريل  ,847 ,24137 ,!,50.000 ,0918742827 ,124
أبوبكر سعيد أبوبكر ,10498-5,35056-5,,40,0915115057,125
ابوبكر صالح ابوبكر ,  ,  ,21913 ,,  ,126
 منير حمد عبدالقادر ,13660 , 954,! , ,0911527923 ,127
منير علي حمد,8366,3751,,,0915745010,128

(  18  )
كشف رقم

اسم السائق,,,رقم الشاحنة,رقم المقطورة,رقم التصريح التعبئة,الحمولة,رقم الهاتف,الرقم ,الاشاري,للشاحنة
جمعة ونيس حمد  , , ,! ,,0924518194,129
 مراجع عبدالسلام مراجع,13798 , 4112, !,,0915444066,130
محمد السنوسي فضل الله ,7616-8 , 5655-3,700442 ,40000 , 0928133583,131
 عبدربه عبدالجليل حميد , , ,!, , 0925944612,132
عادل عوض مفتاح ,1253,10435,!,,0910406664,133
حاتم عمر سويلم محمد ,7735, 973, ,, 0925085054,134
إبراهيم سالم إبراهيم  , , , !, , 0927078095,135
سعيد المبروك سعيد,87,5885,!,50000,0922784133,136

(   19 )
كشف رقم

اسم السائق,,,رقم الشاحنة,رقم المقطورة,رقم التصريح التعبئة,الحمولة,رقم الهاتف,الرقم ,الاشاري,للشاحنة
عبدالرازق ميلاد محمد ,17575 , 18649,702030 ,,0923622420,137
 علي سعيد العجل ,12233-3 , 6888-3, 702051,50,0928031456,138 ,بن جواد
 عبدالعزيز مراجع علي , 43832,34357 , 701977, , 0913322768,139
اشرف عبد الحميد علي  ,  ,  ,02480, ,  ,140
علي محمد خليفه,,,,,,141
 جبريل احمد سعد, , , ,, 0910602603,142
محمد بالعيد يوسف  , , , , ,مساعد ,143
احمد بالقاسم ابراهيم,,,,,مساعد,144

( 20   )
كشف رقم

اسم السائق,,,رقم الشاحنة,رقم المقطورة,رقم التصريح التعبئة,الحمولة,رقم الهاتف,الرقم ,الاشاري,للشاحنة
زيدان عبد الكريم حسن  , , ,13528 ,,,
مسعود محمد فضيل الزوي ,988 ,2283 , !,50000,0910733436,
عماد فرج جمعه  ,41966-5 ,1635-14 ,702084 , , 0926209030,
محمد صالح احمد  ,2081 ,33037 ,!, ,0918181715  ,
عبدالغني محمد محمد  ,9983 ,1940-14 ,@, 40,0913173995 ,
 محمد صالح محمد ابرهيم,35575-5 ,36457-5 ,701493 ,50000, 0924159742,,
 ادريس عبدالكريم سعيد,  ,  , ,  , 0915005889,
خالد ابوبكر محمد,,,!,,,

(  21  )
كشف رقم

اسم السائق,,,رقم الشاحنة,رقم المقطورة,رقم التصريح التعبئة,الحمولة,رقم الهاتف,الرقم ,الاشاري,للشاحنة
المهدي محمد عوض , , ,07387,, ,
 عبد السلام عبد الجواد عبد السلام, , ,23166 ,, ,
اشرف عبدالسلام مفتاح , 1234, 2115, , 40000,0928687651 ,
 زيدان عبدالكريم حسن,13842-8  ,10046-8 ,700940, ,0919778549 ,
محمد سعد جابر ,,,13796,, ,
عمر عبدالمجيد يوسف ,126 , 32631, !,, 0910951947,
أشرف سليمان محمد  ,2306 ,19274 , !, 40000, 0921414337,
اسامه دخيل عبدالسلام,1419,9418,,,0925330476,

( 22   )
كشف رقم

اسم السائق,,,رقم الشاحنة,رقم المقطورة,رقم التصريح التعبئة,الحمولة,رقم الهاتف,الرقم ,الاشاري,للشاحنة
مرعي فرج عمر ,8803 , 3791,! ,50000,0910212580,
حامد نصر حامد ,988  ,2283 , !, , ,
عادل عبدالله ,1132 , 10437, !, 40000, 0914460702,
سعد محمد الشعيب , 2350,2023 ,!,40000 , 0922858097,
عبدالقادر محمد عقيله,13899-8,13336-8,702347,50000,0913829308,
وليد عبدالرازق محمد ,13071-8 , 12886-8,702067 ,40000, 0928029878,
رمضان ابولطيعه حمد , 7900, 7565, ,50000 , 0924626141,
عبد الباسط عبد السلام عيسى ,                  , ,06640 , , ,

(   23 )
كشف رقم

اسم السائق,,,رقم الشاحنة,رقم المقطورة,رقم التصريح التعبئة,الحمولة,رقم الهاتف,الرقم ,الاشاري,للشاحنة
حاتم فرج ونيس محمد ,2195-30 ,10211-8 , ,50 , 0914560083,
محمد بالقاسم سالم  , 9116-8, 18254-25,700091 ,50, 0914709147,
محمد حمد صالح , 9398-8,35961-5 , !, , 0915725023,
حلمي عوض محمد ,  3937-8, 1337-30 ,,40 ,0927080381 ,
المهدي عيسى المهدي ,9511-8, 6372-3,,50,0917354460 ,
مصطفي جمال مصطفي  ,9944-8,34321-5,701676 ,,0920707022,
صقر رمضان علي,,,15577,,,
صهيب رمضان علي ,12455-8,1484-30,701417,40,0919431893,091603036,

( 24   )
كشف رقم ( 25)

اسم السائق,,,رقم الشاحنة,رقم المقطورة,رقم التصريح التعبئة,الحمولة,رقم الهاتف,الرقم ,الاشاري,للشاحنة
فرج موسي جويلي ,49703,39556, ,50,,
صالح حمد صالح ,,,00463,,,
,احمد علي سليمان ,8019,18856,,50.000,0924837659,
احمد ابريك  عبد الحميد ,35-88,14-2021 , 18681, 50.000,0943576186 ,
عبد الله عيد محمد,13301-8,1699-30,,50.000,0910099855,,
صهيب خالد رجب ,,,025508,50000,,
سعد عبدالفتاح عثمان,602-2,1266-14,025507,50.000,0944378812,
فرج عبدالنبي سليمان,,,005893,,,
اسم السائق,رقم الشاحنه,رقم المقطورة,رقم التصريح التعبئة,الحمولة,رقم الهاتف,الرقم الاشاري للشاحنة
الطاهر المهدي امحمد ,,, ,,,
صالح حمد صالح,,,000463,,,
مفتاح حمد صالح,,,000464,,,
معتز محمد خميس,,,025509,,,
هشام فرج محمد,13301-8,35728-5,702201,50,0925305603,
حامد علي محمد,,9546-8,,40,0916401357,0944814793,
 , , ,, , ,
عبدالله عيد محمد,13301-8,1699-30,701701,50,0910099855,0944814793,جديد
مصعب عبدالرحمن رمضان,14169-8,2914-30,702059,40,0916144736,سرير

كشف رقم (26)

اسم السائق,,,رقم الشاحنة,رقم المقطورة,رقم التصريح التعبئة,الحمولة,رقم الهاتف,,ملاحظات
عبدالمنعم فرج خليفة ,14541-8 , 13799-8,702417 ,40,0920550053 ,سرير
انيس عبدالرحيم ونيس  ,41408-5 ,  31913-5,701513 ,40, ,سرير
محمد سالم محمود , , , ,50 , 0913761210,  سرير
حسن جاد الله,  39692-5,33794-5  ,700639 , ,0925666193 ,
محمد عبدالحفيظ مسعود,23-77, 23199-5,700368,50,0914188090,
عبدالناصر محمد الجيلاني,,12073-8 ,12027-8 ,701023 ,50,0924521182 ,
خالد معزوق امبارك  ,828-12 ,33276-5,700236 ,50 ,0913484833  ,
موسي فرج موسي  ,13115-8,2978-30,702162,40,0927354920 ,

كشف رقم (27)

اسم السائق,,,رقم الشاحنة,رقم المقطورة,رقم التصريح التعبئة,الحمولة,رقم الهاتف,,ملاحظات
احمد مصطفي عقيلة ,38146-5 ,13818-5,701020 ,,0925235695 ,
محمود إبراهيم محمد  ,18339-25 ,3719-30  ,702365 ,50,0910020990 ,
صلاح محمد الزروق  ,39632-5 ,39667-5 ,701055 ,50 ,092421259 ,
ابراهيم سعيد ابراهيم ,  13938-8,905-12  ,702385 ,40 ,0925315675  ,
فرج مؤمن شعيب ,37-10,5484-10,702190,50,0913077748,
 عبدالتواب غيث خليفة,937-33 ,38277-5 ,702361 ,40,0916224457 ,صيانة تنك
 صالح عبدالسلام محمد, 332-18,13573-8, 700103, ,0925607282  ,
علي عبد الحميد حمد ,240-36,2101-14,701114,40,0915772105 ,

كشف رقم (28)
كشف رقم

اسم السائق,,,رقم الشاحنة,رقم المقطورة,رقم التصريح التعبئة,الحمولة,رقم الهاتف,,ملاحظات
عبدالله عبد القادرعبدالرحيم,909-6 ,16978-25, 701288,40,0915787790 ,
عبدالفتاح جمعة محمد  , 8594-5,15514-5  ,701467 ,,0944532346 ,
 احمد فرج السنوس, 13691-8,6794-8 ,702268 ,40 ,0925481819 ,يبي يشري تنك
 علي محمد السنوسي,  1536-30,3952-5  ,700989 , ,0913267391  ,
علاء الدين علي  ,9297-8,35690-5,701343,40,0927875947,
حمد بوبكر حمد ,49027-5 ,38582-5 ,702380 ,,0945514535 ,
فرج ميلاد فليفل , 12956-8,15014-25 ,700100 ,50 ,0925336621  ,
ابوبكر سعد ابرهيم ,8734-8,5497-3,701038,40,0944449231 ,

( 29   )
كشف رقم

اسم السائق,,,رقم الشاحنة,رقم المقطورة,رقم التصريح التعبئة,الحمولة,رقم الهاتف,,ملاحظات
علي عبدالحميد حمد ,240-36 ,2101-14 ,701114 ,,0915772105 ,
  علاء منصور خميس,1035-12 ,6755-12  ,701791 ,40, ,
محمد علي فرج , 8573-8,13574-8 ,702402 , ,0925326567 ,
أسامة دخيل عبدالسلام ,  1419-30,9418-8  ,700372 ,50 ,0925330476  ,
 محمد ناجي يونس,18-77,1663-14,702253,40,0926418744,
محمد احمد محمد ,12383-8 , 12844-8, 702258,,0928117505 ,
 خيرالله سليمان داوود,5-73 ,36511-5 ,702205 ,40 ,  ,   !
عبد الحميد مفتاح عامر ,4490-8,2743-30,702183,, ,

( 30 )
كشف رقم

اسم السائق,,,رقم الشاحنة,رقم المقطورة,رقم التصريح التعبئة,الحمولة,رقم الهاتف,,ملاحظات
إبراهيم مفتاح عامر ,7929-8 , 8612-8,701339 ,,0925128427 ,
محمد اشعيب محمد  ,36-46 , 1251-14 ,700508 ,50, 0921147375,
 علاء الدين محمد محمد, 236-17,29-42 ,701906 , ,0924218969 ,
عبدالله رمضان علي ,  12942-8,2819-8,700244 , 50,0922858027  ,
احمد بن ناصر  ,12444,3702,,40,,
عبدالسلام علي محمد  ,1306 ,6761 , ,50, ,
محمد حسين سعيد ,13576 ,13769 , ,50 ,  ,
محمد  حسن محمد ,2306,19274,,40, ,  

( 31   )
كشف رقم

اسم السائق,,,رقم الشاحنة,رقم المقطورة,رقم التصريح التعبئة,الحمولة,رقم الهاتف,,ملاحظات
مرعي علي ابراهيم ,22495 ,5967 , ,50, ,
سالم صالح علي  , 44009, 2200 , ,50, ,
محمد جمعة علي  2,12444 ,3702 , ,40 ,0924544378 ,
 علي مختار علي ,8792,  , , ,  ,!
مختار ادريس مختار ,8792,10224,,50,,
 عادل التركي مجيد  ,5287 ,5885 ,700404 ,50 , 0942760163,0925778337,مشرق
سعد عبدالفتاح عثمان , 602-2,1266-14 ,800232 ,40 ,0944378812  ,مشرق
علي سعيد امراجع ,2108,2429,702431,50,0925497281 ,مشرق ,جديد

( 32  )
كشف رقم

اسم السائق,,,رقم الشاحنة,رقم المقطورة,رقم التصريح التعبئة,الحمولة,رقم الهاتف,,ملاحظات
محمد عبدالواحد  سعد, 13524-8, 33270-5, ,40,0920419739 ,غيث
معتز طارق منصور  ,1496-30 ,  21352-5, 701333,40,0944112129 ,سائق جديد ,كانت مفوزة
حمد فتحي حمد ,12253-21 ,701-30 ,702450 ,50 ,0940009981 ,جبل واجدابيا,زحمة لا
حسام عبدالله محمد ,  14531-5,18778-25  , 702008,50 ,  0910832920,جديد  من مغرب,عمل قمينس من التواصل سابقا
 ,,,,,,
 , , , ,, ,
 , , , , ,  ,
 ,,,,, ,

( 33)
كشف رقم

 , , , ,, ,
  , ,  , ,, ,
 , , , , , ,
 ,  ,  , , ,  ,
 ,,,,,,
 , , , ,, ,
 , , , , ,  ,
 ,,,,, ,
`;


        // Function to parse the uploaded document content and assign sequential IDs
        function parseDriversDocument(text) {
            const lines = text.split('\n');
            const parsedDrivers = [];
            let currentId = 1; // Start ID from 1 for parsed data

            lines.forEach(line => {
                // Skip header lines and "كشف رقم" lines, and empty lines
                if (line.includes('اسم السائق') || line.includes('كشف رقم') || line.trim() === '') {
                    return;
                }

                // Split by comma, trim whitespace, and remove '!' or '@'
                const parts = line.split(',').map(part => part.trim().replace(/[!@]/g, ''));

                // Filter out any empty strings resulting from the split/trimming
                const cleanedParts = parts.filter(part => part !== '');

                // Skip lines that don't have enough parts for basic info (at least a name and something else)
                if (cleanedParts.length < 2) {
                    return;
                }

                let name = cleanedParts[0];
                let phone = '';
                let truck = '';
                let trailer = '';
                let permit = '';
                let notes = ''; // To capture potential notes at the end

                // Attempt to extract Phone Number - look for parts starting with 09 or 05
                let phoneFoundIndex = -1;
                // Search for phone number starting from index 1 (after Name)
                for (let i = 1; i < cleanedParts.length; i++) {
                     const part = cleanedParts[i];
                     // Check if the part looks like a phone number (starts with 09 or 05, mostly digits)
                     if (/^0[95]\d+$/.test(part.replace(/\D/g, ''))) {
                        phone = part;
                        phoneFoundIndex = i;
                        break; // Take the first phone number found
                     }
                }

                 // Extract Truck, Trailer, Permit, and potential Notes from parts after Name and before Phone (if found) or at the end
                 const startIndexForMiddle = 1;
                 let endIndexForMiddle = cleanedParts.length; // Default to the end

                 if (phoneFoundIndex !== -1) {
                     endIndexForMiddle = phoneFoundIndex;
                 }

                 const fieldsBetween = cleanedParts.slice(startIndexForMiddle, endIndexForMiddle);

                 // Assign the middle fields to Truck, Trailer, Permit sequentially
                 truck = fieldsBetween[0] || '';
                 trailer = fieldsBetween[1] || '';
                 permit = fieldsBetween[2] || '';

                 // Capture any remaining parts after the phone number as notes
                 if (phoneFoundIndex !== -1 && phoneFoundIndex < cleanedParts.length - 1) {
                     notes = cleanedParts.slice(phoneFoundIndex + 1).join(', ');
                 } else if (phoneFoundIndex === -1 && cleanedParts.length > startIndexForMiddle + 3) {
                    // If no phone found, and there are more than 3 fields after name, assume remaining are notes
                     notes = cleanedParts.slice(startIndexForMiddle + 3).join(', ');
                 }


                // Create the driver object
                const driver = {
                    id: currentId, // Assign sequential ID
                    name: name || 'غير محدد',
                    phone: phone || '',
                    truck: truck,
                    trailer: trailer,
                    permit: permit,
                    permitImage: "", // No image in the provided text
                    status: "سائق جديد", // Default status for new entries
                    lastDelivery: { station: "", date: "" }, // Default empty last delivery info
                    notes: notes // Store any potential notes
                };

                parsedDrivers.push(driver);
                currentId++; // Increment sequential ID for the next driver
            });

             // No need to remove duplicates based on original ID since we're assigning new sequential ones
            return parsedDrivers;
        }


        // Function to save drivers data to localStorage
        function saveDrivers() {
            localStorage.setItem(DRIVERS_LOCAL_STORAGE_KEY, JSON.stringify(drivers));
        }

        // Function to load drivers data from localStorage
        function loadDrivers() {
            const data = localStorage.getItem(DRIVERS_LOCAL_STORAGE_KEY);
            if (data) {
                drivers = JSON.parse(data);
            } else {
                 // If no data in localStorage, parse the uploaded document content
                 drivers = parseDriversDocument(uploadedDocumentContent);
                 saveDrivers(); // Save the parsed data to localStorage initially
            }
        }

        // Function to format phone number for WhatsApp
        function formatPhoneNumberForWhatsApp(phoneNumber) {
            // Remove any non-digit characters
            const digitsOnly = phoneNumber.replace(/\D/g, '');

            // Find the index of the first '9'
            const firstNineIndex = digitsOnly.indexOf('9');

            // If '9' is found and it's not the last digit, take the part after '9'
            if (firstNineIndex !== -1 && firstNineIndex < digitsOnly.length - 1) {
                 const numberAfterNine = digitsOnly.substring(firstNineIndex + 1);
                 return `2189${numberAfterNine}`; // Prepend 2189
            }

            // Fallback: If '9' is not found or is the last digit, try removing leading zero if present and prepend 218
            if (digitsOnly.startsWith('0')) {
                return `218${digitsOnly.substring(1)}`;
            }

            // If no '9' and no leading zero, just prepend 218
            return `218${digitsOnly}`;
        }


        // Function to render the drivers table with optional status filter
        function renderDrivers(filter = '', statusFilter = '') {
            driversTableBody.innerHTML = ''; // Clear existing rows

            // Apply text filter first
            let filteredDrivers = drivers.filter(driver =>
                driver.name.toLowerCase().includes(filter.toLowerCase()) ||
                driver.phone.includes(filter) ||
                driver.truck.toLowerCase().includes(filter.toLowerCase()) ||
                driver.trailer.toLowerCase().includes(filter.toLowerCase()) ||
                driver.permit.toLowerCase().includes(filter.toLowerCase()) ||
                driver.status.toLowerCase().includes(filter.toLowerCase()) ||
                (driver.lastDelivery.station && driver.lastDelivery.station.toLowerCase().includes(filter.toLowerCase())) ||
                (driver.notes && driver.notes.toLowerCase().includes(filter.toLowerCase())) // Include notes in search
            );

            // Apply status filter if provided
            if (statusFilter && statusFilter !== 'all') {
                filteredDrivers = filteredDrivers.filter(driver => driver.status === statusFilter);
                 showAllBtn.classList.remove('hidden'); // Show "Show All" button
            } else {
                 showAllBtn.classList.add('hidden'); // Hide "Show All" button
            }


            filteredDrivers.forEach(driver => {
                const row = document.createElement('tr');
                row.classList.add('hover:bg-gray-100'); // Add hover effect
                row.setAttribute('data-status', driver.status); // Add data attribute for status

                // Determine status color class
                const statusClass = `status-${driver.status.replace(/\s+/g, '-')}`;

                // Format phone number for WhatsApp
                const whatsappFormattedPhone = driver.phone ? formatPhoneNumberForWhatsApp(driver.phone) : '';


                row.innerHTML = `
                    <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-sm text-gray-800">${driver.id}</td>
                    <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-sm text-gray-800">${driver.name}</td>
                    <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-sm text-gray-800">
                        ${driver.phone ? `<a href="tel:${driver.phone}" class="text-blue-600 hover:underline">${driver.phone}</a>` : 'لا يوجد رقم'}
                    </td>
                    <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-sm text-gray-800 no-print">
                        ${whatsappFormattedPhone ?
                            `<a href="https://wa.me/${whatsappFormattedPhone}" target="_blank" class="whatsapp-btn">
                                <i class="fab fa-whatsapp"></i> واتساب
                            </a>`
                            : 'N/A' // Or handle cases where formatting fails
                         }
                    </td>
                    <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-sm text-gray-800">${driver.truck}</td>
                    <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-sm text-gray-800">${driver.trailer}</td>
                    <td class="px-3 py-2 sm:px-6 sm:py-4 text-sm text-gray-800">
                        ${driver.permit ? driver.permit : ''}
                        ${driver.permitImage ?
                            `<button onclick="openImageModal('${driver.permitImage}')" class="text-blue-600 hover:underline ml-1 focus:outline-none"><i class="fas fa-image"></i></button>`
                            : ''
                         }
                    </td>
                    <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-sm font-medium ${statusClass} rounded-full text-center">
                        ${driver.status}
                    </td>
                    <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-sm text-gray-800">
                        ${driver.lastDelivery && driver.lastDelivery.station ? `${driver.lastDelivery.station} (${driver.lastDelivery.date})` : (driver.notes ? `ملاحظات: ${driver.notes}` : 'لا يوجد')}
                    </td>
                    <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-right text-sm font-medium no-print">
                        <button onclick="editDriver(${driver.id})" class="text-indigo-600 hover:text-indigo-900 ml-2">
                            <i class="fas fa-edit"></i> تعديل
                        </button>
                        <button onclick="deleteDriver(${driver.id})" class="text-red-600 hover:text-red-900">
                            <i class="fas fa-trash-alt"></i> حذف
                        </button>
                    </td>
                `;
                driversTableBody.appendChild(row);
            });
        }

        // Function to update driver summary counts
        function updateDriversSummaries() {
            const availableCount = drivers.filter(driver => driver.status === 'متاح').length;
            const busyCount = drivers.filter(driver => driver.status === 'مشغول').length;
            const maintenanceCount = drivers.filter(driver => driver.status === 'صيانة').length;
            const absentCount = drivers.filter(driver => driver.status === 'غير موجود').length;
            const newCount = drivers.filter(driver => driver.status === 'سائق جديد').length;

            if(totalAvailableEl) totalAvailableEl.textContent = availableCount;
            if(totalBusyEl) totalBusyEl.textContent = busyCount;
            if(totalMaintenanceEl) totalMaintenanceEl.textContent = maintenanceCount;
            if(totalAbsentEl) totalAbsentEl.textContent = absentCount;
            if(totalNewEl) totalNewEl.textContent = newCount;
            if(document.getElementById('totalDriversStat')) {
                 document.getElementById('totalDriversStat').textContent = drivers.length;
            }
        }

        // Function to open modal for adding a new driver
        function openAddModal() {
            modalTitleEl.textContent = 'إضافة سائق جديد';
            submitDriverBtn.textContent = 'إضافة';
            driverIdInput.value = ''; // Clear hidden ID for add (ID is assigned on save)
            driverForm.reset(); // Reset form fields
            currentPermitImagePreview.classList.add('hidden'); // Hide image preview for add
            currentPermitImagePreview.src = ''; // Clear image preview src
            driverModal.classList.remove('hidden');
        }

        // Function to open modal for editing a driver
        function editDriver(id) {
            const driver = drivers.find(d => d.id === id);
            if (driver) {
                modalTitleEl.textContent = `تعديل بيانات السائق: ${driver.name}`;
                submitDriverBtn.textContent = 'حفظ التعديلات';
                driverIdInput.value = driver.id; // Set hidden ID
                driverNameInput.value = driver.name;
                driverPhoneInput.value = driver.phone;
                driverTruckInput.value = driver.truck;
                driverTrailerInput.value = driver.trailer;
                driverPermitInput.value = driver.permit;

                // Handle permit image preview
                if (driver.permitImage) {
                    currentPermitImagePreview.src = driver.permitImage;
                    currentPermitImagePreview.classList.remove('hidden');
                } else {
                    currentPermitImagePreview.classList.add('hidden');
                    currentPermitImagePreview.src = '';
                }

                driverStatusInput.value = driver.status;
                driverLastDeliveryStationInput.value = driver.lastDelivery ? driver.lastDelivery.station : '';
                driverLastDeliveryDateInput.value = driver.lastDelivery ? driver.lastDelivery.date : '';


                driverModal.classList.remove('hidden');
            }
        }

         // Function to delete a driver
         function deleteDriver(id) {
             if (confirm('هل أنت متأكد أنك تريد حذف هذا السائق؟')) {
                 drivers = drivers.filter(driver => driver.id !== id);
                 saveDrivers(); // Save data after deletion
                 renderDrivers(searchInput.value); // Re-render table with current filter
                 updateDriversSummaries(); // Update summaries
             }
         }


        // Function to handle driver form submission (Add or Edit)
        function handleDriverFormSubmit(e) {
            e.preventDefault(); // Prevent default form submission

            const id = driverIdInput.value ? parseInt(driverIdInput.value) : null; // Parse ID as integer
            const name = driverNameInput.value;
            const phone = driverPhoneInput.value;
            const truck = driverTruckInput.value;
            const trailer = driverTrailerInput.value;
            const permit = driverPermitInput.value;
            const status = driverStatusInput.value;
            const lastDeliveryStation = driverLastDeliveryStationInput.value;
            const lastDeliveryDate = driverLastDeliveryDateInput.value;
            const permitFile = driverPermitImageInput.files[0]; // Get the selected file

            // Function to finalize save/update after image is read
            const finalizeSave = (permitImageData = '') => {
                 if (id !== null) { // Editing existing driver
                    drivers = drivers.map(driver =>
                        driver.id === id ? {
                            ...driver,
                            name,
                            phone,
                            truck,
                            trailer,
                            permit,
                            // Use new image data if provided, otherwise keep existing
                            permitImage: permitImageData || driver.permitImage,
                            status,
                            lastDelivery: { station: lastDeliveryStation, date: lastDeliveryDate }
                        } : driver
                    );
                } else { // Adding new driver
                     // Calculate the next sequential ID for a new driver
                    const nextId = drivers.length > 0 ? Math.max(...drivers.map(d => d.id)) + 1 : 1;
                    const newDriver = {
                        id: nextId, // Assign the next sequential ID
                        name,
                        phone,
                        truck,
                        trailer,
                        permit,
                        permitImage: permitImageData, // Use the read image data
                        status,
                        lastDelivery: { station: lastDeliveryStation, date: lastDeliveryDate }
                    };
                    drivers.push(newDriver);
                }

                saveDrivers(); // Save data after add/edit
                renderDrivers(searchInput.value); // Re-render table with current filter
                updateDriversSummaries(); // Update summaries

                // Hide the modal and reset the form
                driverModal.classList.add('hidden');
                driverForm.reset();
                 currentPermitImagePreview.classList.add('hidden'); // Hide preview after saving
                 currentPermitImagePreview.src = ''; // Clear preview src
            };


            if (permitFile) {
                // Read the file if one is selected
                const reader = new FileReader();
                reader.onloadend = () => {
                    // reader.result contains the Base64 string
                    finalizeSave(reader.result);
                };
                reader.readAsDataURL(permitFile); // Read file as Data URL (Base64)
            } else {
                 // If no new file is selected, but there was an existing image, keep it
                 const existingDriver = drivers.find(d => d.id === id);
                 finalizeSave(existingDriver ? existingDriver.permitImage : '');
            }
        }

        // Function to backup driver data
        function backupData() {
            const dataStr = JSON.stringify(drivers, null, 2); // Pretty print JSON
            const blob = new Blob([dataStr], { type: 'application/json' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'drivers_backup_' + new Date().toISOString().split('T')[0] + '.json';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url); // Clean up
        }

        // Function to open the image modal
        function openImageModal(imageData) {
            fullPermitImage.src = imageData;
            imageModal.classList.remove('hidden');
        }

        // Function to close the image modal
        function closeImageModal() {
            imageModal.classList.add('hidden');
            fullPermitImage.src = ''; // Clear the image source
        }

        // Function to handle printing based on selected scope
        function handlePrint() {
            const selectedScope = document.querySelector('input[name="printScope"]:checked').value;

            // Hide non-printable elements
            document.querySelectorAll('.no-print').forEach(el => el.style.display = 'none');

            // Create a temporary container for the printable table
            const printableContainer = document.createElement('div');
            printableContainer.id = 'printable-table-container';
            document.body.appendChild(printableContainer);

            // Clone the table header
            const tableHeader = driversTable.querySelector('thead').cloneNode(true);
            printableContainer.appendChild(tableHeader);

            // Create and populate the printable table body
            const printableTableBody = document.createElement('tbody');
             // Copy classes from original tbody for styling
            printableTableBody.className = driversTableBody.className;


            drivers.forEach(driver => {
                // Check if the driver matches the selected scope
                if (selectedScope === 'all' || driver.status === selectedScope) {
                    const row = document.createElement('tr');
                     // Copy classes from original rows for styling
                    row.className = driversTableBody.querySelector('tr')?.className || '';
                    row.setAttribute('data-status', driver.status); // Keep status data attribute

                     // Determine status color class for print
                    const statusClass = `status-${driver.status.replace(/\s+/g, '-')}`;

                    row.innerHTML = `
                        <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-sm text-gray-800">${driver.id}</td>
                        <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-sm text-gray-800">${driver.name}</td>
                        <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-sm text-gray-800">${driver.phone}</td>
                        <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-sm text-gray-800"></td>
                        <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-sm text-gray-800">${driver.truck}</td>
                        <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-sm text-gray-800">${driver.trailer}</td>
                        <td class="px-3 py-2 sm:px-6 sm:py-4 text-sm text-gray-800">${driver.permit ? driver.permit : ''}</td>
                        <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-sm font-medium ${statusClass} rounded-full text-center">${driver.status}</td>
                        <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-sm text-gray-800">
                            ${driver.lastDelivery && driver.lastDelivery.station ? `${driver.lastDelivery.station} (${driver.lastDelivery.date})` : (driver.notes ? `ملاحظات: ${driver.notes}` : 'لا يوجد')}
                        </td>
                        <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-right text-sm font-medium"></td> `;
                    printableTableBody.appendChild(row);
                }
            });

             // Create the printable table structure
            const printableTable = document.createElement('table');
             // Copy classes from original table for styling
            printableTable.className = driversTable.className;
            printableTable.appendChild(tableHeader);
            printableTable.appendChild(printableTableBody);
            printableContainer.appendChild(printableTable);


            // Trigger print
            window.print();

            // Clean up: remove the temporary container and show hidden elements
            document.body.removeChild(printableContainer);
            document.querySelectorAll('.no-print').forEach(el => el.style.display = ''); // Restore display

            // Close the print options modal
            printOptionsModal.classList.add('hidden');
        }


        // --- End of Existing JavaScript from astol.html (for Drivers) ---


        // --- Start of New JavaScript for Stations ---

        // Key for localStorage for Stations
        const STATIONS_LOCAL_STORAGE_KEY = 'fuelStationsData';

        // Array to hold station data
        let stations = [];

        // Get table body element for Stations
        const stationsTableBody = document.getElementById('stations-table-body');

        // Get add/edit modal elements for Stations
        const stationModal = document.getElementById('station-modal');
        const stationModalTitleEl = document.getElementById('station-modal-title');
        const addStationBtn = document.getElementById('add-station-btn');
        const closeStationModalBtn = document.getElementById('close-station-modal-btn');
        const stationForm = document.getElementById('station-form');
        const submitStationBtn = document.getElementById('submit-station-btn');
        const stationIdInput = document.getElementById('station-id');
        // Get form inputs for Stations
        const stationCompanyInput = document.getElementById('station-company'); // New: Company input
        const stationNameInput = document.getElementById('station-name');
        const stationNumberInput = document.getElementById('station-number'); // New: Station Number input
        const stationAddressInput = document.getElementById('station-address');
        const stationOwnerInput = document.getElementById('station-owner');
        const stationPhoneInput = document.getElementById('station-phone');


        // Function to save stations data to localStorage
        function saveStations() {
            localStorage.setItem(STATIONS_LOCAL_STORAGE_KEY, JSON.stringify(stations));
        }

        // Function to load stations data from localStorage
        function loadStations() {
            const data = localStorage.getItem(STATIONS_LOCAL_STORAGE_KEY);
            if (data) {
                stations = JSON.parse(data);
            } else {
                stations = []; // Start with an empty array if no data
            }
        }

        // Function to render the stations table
        function renderStations() {
            stationsTableBody.innerHTML = ''; // Clear existing rows

            stations.forEach(station => {
                const row = document.createElement('tr');
                row.classList.add('hover:bg-gray-100'); // Add hover effect

                // Check if there's an active order for this station
                const isDelivering = orders.some(order => order.stationId === station.id);
                const deliveryStatusHtml = isDelivering ?
                    '<span class="delivery-status-indicator delivering" title="يتم التوصيل حالياً"></span>' :
                    '';


                row.innerHTML = `
                    <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-sm text-gray-800">${station.id}</td>
                    <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-sm text-gray-800">${station.company || ''}</td>
                    <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-sm text-gray-800">${station.name}</td>
                    <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-sm text-gray-800">${station.stationNumber || ''}</td> <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-sm text-gray-800">${station.address || ''}</td>
                    <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-sm text-gray-800">${station.owner || ''}</td>
                    <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-sm text-gray-800">${station.phone || ''}</td>
                    <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-center text-sm text-gray-800">
                        ${deliveryStatusHtml}
                    </td>
                    <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-right text-sm font-medium no-print">
                        <button onclick="editStation(${station.id})" class="text-indigo-600 hover:text-indigo-900 ml-2">
                            <i class="fas fa-edit"></i> تعديل
                        </button>
                        <button onclick="deleteStation(${station.id})" class="text-red-600 hover:text-red-900">
                            <i class="fas fa-trash-alt"></i> حذف
                        </button>
                    </td>
                `;
                stationsTableBody.appendChild(row);
            });
        }

        // Function to open modal for adding a new station
        function openAddStationModal() {
            stationModalTitleEl.textContent = 'إضافة محطة جديدة';
            submitStationBtn.textContent = 'إضافة';
            stationIdInput.value = ''; // Clear hidden ID for add
            stationForm.reset(); // Reset form fields
            stationModal.classList.remove('hidden');
        }

        // Function to open modal for editing a station
        function editStation(id) {
            const station = stations.find(s => s.id === id);
            if (station) {
                stationModalTitleEl.textContent = `تعديل بيانات المحطة: ${station.name}`;
                submitStationBtn.textContent = 'حفظ التعديلات';
                stationIdInput.value = station.id; // Set hidden ID
                stationCompanyInput.value = station.company || ''; // Set company value
                stationNameInput.value = station.name;
                stationNumberInput.value = station.stationNumber || ''; // Set station number value
                stationAddressInput.value = station.address;
                stationOwnerInput.value = station.owner;
                stationPhoneInput.value = station.phone;

                stationModal.classList.remove('hidden');
            }
        }

        // Function to delete a station
         function deleteStation(id) {
             if (confirm('هل أنت متأكد أنك تريد حذف هذه المحطة؟')) {
                 stations = stations.filter(station => station.id !== id);
                 saveStations(); // Save data after deletion
                 renderStations(); // Re-render table
                  // Also re-render orders table in case this station was linked
                 renderOrders(orderSearchInput.value); // Re-render orders table with current search filter
             }
         }


        // Function to handle station form submission (Add or Edit)
        function handleStationFormSubmit(e) {
            e.preventDefault(); // Prevent default form submission

            const id = stationIdInput.value ? parseInt(stationIdInput.value) : null; // Parse ID as integer
            const company = stationCompanyInput.value; // Get company value
            const name = stationNameInput.value;
            const stationNumber = stationNumberInput.value; // Get station number value
            const address = stationAddressInput.value;
            const owner = stationOwnerInput.value;
            const phone = stationPhoneInput.value;

            if (id !== null) { // Editing existing station
                stations = stations.map(station =>
                    station.id === id ? {
                        ...station,
                        company, // Save company
                        name,
                        stationNumber, // Save station number
                        address,
                        owner,
                        phone
                    } : station
                );
            } else { // Adding new station
                 // Calculate the next sequential ID for a new station
                const nextId = stations.length > 0 ? Math.max(...stations.map(s => s.id)) + 1 : 1;
                const newStation = {
                    id: nextId, // Assign the next sequential ID
                    company, // Save company
                    name,
                    stationNumber, // Save station number
                    address,
                    owner,
                    phone
                };
                stations.push(newStation);
            }

            saveStations(); // Save data after add/edit
            renderStations(); // Re-render table

            // Hide the modal and reset the form
            stationModal.classList.add('hidden');
            stationForm.reset();
             // Re-populate order form dropdowns in case a new station was added
            populateOrderFormDropdowns();
        }

        // --- End of New JavaScript for Stations ---


        // --- Start of New JavaScript for Orders ---

        // Key for localStorage for Orders
        const ORDERS_LOCAL_STORAGE_KEY = 'fuelOrdersData';

        // Array to hold order data
        let orders = [];

        // Get table body element for Orders
        const ordersTableBody = document.getElementById('orders-table-body');

        // Get order form elements
        const orderForm = document.getElementById('order-form');
        const orderWarehouseInput = document.getElementById('order-warehouse');
        const orderCompanyInput = document.getElementById('order-company');
        const orderNotificationIdInput = document.getElementById('order-notification-id');
        const orderDateInput = document.getElementById('order-date');
        const orderFuelTypeInput = document.getElementById('order-fuel-type');
        const orderQuantityInput = document.getElementById('order-quantity');
        const orderStationInput = document.getElementById('order-station');
        const orderDriverInput = document.getElementById('order-driver');
         // Get search input for Orders
        const orderSearchInput = document.getElementById('order-search-input');
        // Get orders summary stat element on dashboard
        const ordersSummaryStatEl = document.getElementById('ordersSummaryStat');


        // Function to save orders data to localStorage
        function saveOrders() {
            localStorage.setItem(ORDERS_LOCAL_STORAGE_KEY, JSON.stringify(orders));
        }

        // Function to load orders data from localStorage
        function loadOrders() {
            const data = localStorage.getItem(ORDERS_LOCAL_STORAGE_KEY);
            if (data) {
                orders = JSON.parse(data);
            } else {
                orders = []; // Start with an empty array if no data
            }
        }

         // Function to populate dropdowns in the order form
        function populateOrderFormDropdowns() {
            // Populate Stations dropdown
            orderStationInput.innerHTML = '<option value="">اختر المحطة</option>'; // Reset
            stations.forEach(station => {
                const option = document.createElement('option');
                option.value = station.id; // Use station ID as value
                option.textContent = station.name;
                orderStationInput.appendChild(option);
            });

            // Populate Drivers dropdown
            orderDriverInput.innerHTML = '<option value="">اختر السائق</option>'; // Reset
            drivers.forEach(driver => {
                const option = document.createElement('option');
                option.value = driver.id; // Use driver ID as value
                option.textContent = driver.name;
                orderDriverInput.appendChild(option);
            });
        }


        // Function to render the orders table with optional search filter
        function renderOrders(filter = '') {
            ordersTableBody.innerHTML = ''; // Clear existing rows

             // Apply text filter
            const lowerCaseFilter = filter.toLowerCase();
            const filteredOrders = orders.filter(order => {
                // Find the station name for filtering
                const station = stations.find(s => s.id === order.stationId);
                const stationName = station ? station.name.toLowerCase() : '';

                 // Find the driver name for filtering
                const driver = drivers.find(d => d.id === order.driverId);
                const driverName = driver ? driver.name.toLowerCase() : '';

                return (
                    stationName.includes(lowerCaseFilter) ||
                    order.notificationId.toLowerCase().includes(lowerCaseFilter) ||
                    driverName.includes(lowerCaseFilter)
                );
            });


            filteredOrders.forEach(order => {
                const row = document.createElement('tr');
                row.classList.add('hover:bg-gray-100'); // Add hover effect
                row.setAttribute('data-order-id', order.id); // Add data attribute for order ID

                // Find the station name
                const station = stations.find(s => s.id === order.stationId);
                const stationName = station ? station.name : 'محطة غير معروفة';

                 // Find the driver name
                const driver = drivers.find(d => d.id === order.driverId);
                const driverName = driver ? driver.name : 'سائق غير معروف';


                row.innerHTML = `
                    <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-sm text-gray-800">${order.id}</td>
                    <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-sm text-gray-800 editable-cell" data-field="warehouse">${order.warehouse}</td>
                    <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-sm text-gray-800 editable-cell" data-field="company">${order.company}</td>
                    <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-sm text-gray-800 editable-cell" data-field="notificationId">${order.notificationId}</td>
                    <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-sm text-gray-800 editable-cell" data-field="date">${order.date}</td>
                    <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-sm text-gray-800 editable-cell" data-field="fuelType">${order.fuelType}</td>
                    <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-sm text-gray-800 editable-cell" data-field="quantity">${order.quantity}</td>
                    <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-sm text-gray-800 editable-cell" data-field="stationId" data-value="${order.stationId}">${stationName}</td>
                    <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-sm text-gray-800 editable-cell" data-field="driverId" data-value="${order.driverId}">${driverName}</td>
                    <td class="px-3 py-2 sm:px-6 sm:py-4 whitespace-nowrap text-right text-sm font-medium no-print">
                        <button onclick="deleteOrder(${order.id})" class="text-red-600 hover:text-red-900">
                            <i class="fas fa-trash-alt"></i> حذف
                        </button>
                    </td>
                `;
                ordersTableBody.appendChild(row);
            });
        }

        // Function to handle order form submission (Add new order)
        function handleOrderFormSubmit(e) {
            e.preventDefault(); // Prevent default form submission

            // Calculate the next sequential ID for a new order
            const nextId = orders.length > 0 ? Math.max(...orders.map(o => o.id)) + 1 : 1;

            const newOrder = {
                id: nextId, // Assign the next sequential ID
                warehouse: orderWarehouseInput.value,
                company: orderCompanyInput.value,
                notificationId: orderNotificationIdInput.value,
                date: orderDateInput.value,
                fuelType: orderFuelTypeInput.value,
                quantity: orderQuantityInput.value,
                stationId: parseInt(orderStationInput.value), // Store station ID as integer
                driverId: parseInt(orderDriverInput.value) // Store driver ID as integer
            };

            orders.push(newOrder);
            saveOrders(); // Save data after adding
            renderOrders(orderSearchInput.value); // Re-render table with current search filter
            orderForm.reset(); // Reset form after submission
             // Re-render stations table to update delivery status indicators
            renderStations();
            updateOrdersSummary(); // Update the orders summary on the dashboard
        }

        // Function to delete an order
         function deleteOrder(id) {
             if (confirm('هل أنت متأكد أنك تريد حذف هذه الطلبية؟')) {
                 orders = orders.filter(order => order.id !== id);
                 saveOrders(); // Save data after deletion
                 renderOrders(orderSearchInput.value); // Re-render table with current search filter
                  // Re-render stations table to update delivery status indicators
                 renderStations();
                 updateOrdersSummary(); // Update the orders summary on the dashboard
             }
         }

        // Function to update the orders summary on the dashboard
        function updateOrdersSummary() {
            if (!ordersSummaryStatEl) return; // Exit if the element doesn't exist

            // Count orders per company
            const companyCounts = {};
            orders.forEach(order => {
                const station = stations.find(s => s.id === order.stationId);
                if (station && station.company) {
                    const company = station.company;
                    companyCounts[company] = (companyCounts[company] || 0) + 1;
                } else {
                     // Handle orders without a linked station or company if necessary
                     companyCounts['غير محدد'] = (companyCounts['غير محدد'] || 0) + 1;
                }
            });

            // Format the summary string
            let summaryText = 'الطلبيات: ';
            const companySummaries = Object.keys(companyCounts).map(company => {
                return `${company} (${companyCounts[company]})`;
            });

            if (companySummaries.length > 0) {
                summaryText += companySummaries.join(' | '); // Join with '|'
            } else {
                summaryText += 'لا توجد طلبيات';
            }


            ordersSummaryStatEl.textContent = summaryText;
        }


        // Function to handle inline editing for orders table
        function handleOrderTableEdit(e) {
            const cell = e.target.closest('.editable-cell');
            if (!cell) return; // Not an editable cell

            const orderId = parseInt(cell.closest('tr').getAttribute('data-order-id'));
            const field = cell.getAttribute('data-field');
            const originalValue = cell.textContent.trim();
             const originalDataValue = cell.getAttribute('data-value'); // Get original data value for selects

            // Prevent editing if already in edit mode
            if (cell.querySelector('input, select')) return;

            let inputElement;

            // Determine the type of input based on the field
            if (field === 'warehouse') {
                 inputElement = document.createElement('select');
                 inputElement.innerHTML = `
                    <option value="السرير">السرير</option>
                    <option value="راس المنقار">راس المنقار</option>
                 `;
                 inputElement.value = originalValue;
            } else if (field === 'company') {
                 inputElement = document.createElement('select');
                 inputElement.innerHTML = `
                    <option value="الشرارة">الشرارة</option>
                    <option value="الطرق السريعة">الطرق السريعة</option>
                    <option value="البريقة">البريقة</option>
                    <option value="ليبيا نفط">ليبيا نفط</option>
                 `;
                 inputElement.value = originalValue;
            } else if (field === 'date') {
                 inputElement = document.createElement('input');
                 inputElement.type = 'date';
                 inputElement.value = originalValue;
            } else if (field === 'fuelType') {
                 inputElement = document.createElement('select');
                 inputElement.innerHTML = `
                    <option value="بنزين">بنزين</option>
                    <option value="ديزل">ديزل</option>
                 `;
                 inputElement.value = originalValue;
            } else if (field === 'quantity') {
                 inputElement = document.createElement('select');
                 inputElement.innerHTML = `
                    <option value="50000">50,000</option>
                    <option value="40000">40,000</option>
                    <option value="20000">20,000</option>
                    <option value="10000">10,000</option>
                 `;
                 inputElement.value = originalValue;
            } else if (field === 'stationId') {
                 inputElement = document.createElement('select');
                 // Populate with stations
                 stations.forEach(station => {
                     const option = document.createElement('option');
                     option.value = station.id;
                     option.textContent = station.name;
                     inputElement.appendChild(option);
                 });
                 inputElement.value = originalDataValue; // Set value to the station ID
            } else if (field === 'driverId') {
                 inputElement = document.createElement('select');
                 // Populate with drivers
                 drivers.forEach(driver => {
                     const option = document.createElement('option');
                     option.value = driver.id;
                     option.textContent = driver.name;
                     inputElement.appendChild(option);
                 });
                 inputElement.value = originalDataValue; // Set value to the driver ID
            }
            else { // Default to text input for other fields
                inputElement = document.createElement('input');
                inputElement.type = 'text';
                inputElement.value = originalValue;
            }


            // Replace cell content with input element
            cell.textContent = '';
            cell.appendChild(inputElement);
            inputElement.focus();

            // Save changes when input loses focus
            inputElement.addEventListener('blur', () => {
                const newValue = inputElement.value;

                // Find the order in the array
                const orderIndex = orders.findIndex(order => order.id === orderId);
                if (orderIndex > -1) {
                    // Update the order data
                    if (field === 'stationId' || field === 'driverId') {
                         // For select fields, update the stored ID
                         orders[orderIndex][field] = parseInt(newValue);
                    } else {
                        orders[orderIndex][field] = newValue;
                    }

                    saveOrders(); // Auto-save to localStorage
                    renderOrders(orderSearchInput.value); // Re-render the table to show updated value (and potentially linked names) with current search filter
                     // Re-render stations table to update delivery status indicators
                    renderStations();
                    updateOrdersSummary(); // Update the orders summary on the dashboard
                }
            });

             // Optional: Save changes when Enter key is pressed
            inputElement.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') {
                    inputElement.blur(); // Trigger blur to save
                }
            });
        }


        // --- End of New JavaScript for Orders ---


        // --- Event Listeners ---

        // Load data and render on page load
        window.onload = () => {
             loadDrivers(); // Load driver data
             loadStations(); // Load station data
             loadOrders(); // Load order data

             // Initial rendering and summary update will happen when the respective tabs are first shown
             updateDriversSummaries(); // Update driver summary counts on initial load for the dashboard stat
             updateOrdersSummary(); // Update the orders summary on initial load for the dashboard stat
             document.getElementById('currentYear').textContent = new Date().getFullYear();

             // Add event listener to the dashboard stat card for drivers
             const totalDriversCard = document.querySelector('.stat-card.bg-blue-600[data-tab="drivers"]');
             if (totalDriversCard) {
                 totalDriversCard.addEventListener('click', () => {
                     showTab('drivers'); // Switch to the drivers tab when clicked
                 });
             }

             // Simulate truck movement on the map (basic animation) - Keep existing animation if needed
             if (document.getElementById('tracking')) {
                 function animateTrucks() {
                     const truckElements = document.querySelectorAll('#tracking .truck-icon');
                     truckElements.forEach(truck => {
                         if (truck.innerHTML.includes('fa-truck')) {
                             const randomX = Math.floor(Math.random() * 6) - 3;
                             const randomY = Math.floor(Math.random() * 6) - 3;
                             let currentTop = parseInt(truck.style.top) || 0;
                             let currentRight = parseInt(truck.style.right) || 0;
                             const mapContainer = truck.closest('.map-container');
                             if (mapContainer) {
                                 const mapHeight = mapContainer.clientHeight;
                                 const mapWidth = mapContainer.clientWidth;
                                 currentTop = Math.max(10, Math.min(currentTop + randomY, mapHeight - 40));
                                 currentRight = Math.max(10, Math.min(currentRight + randomX, mapWidth - 40));
                             }
                             truck.style.top = `${currentTop}px`;
                             truck.style.right = `${currentRight}px`;
                         }
                     });
                 }
                 // Start animation only if the tracking tab exists
                 if (document.getElementById('tracking')) {
                    setInterval(animateTrucks, 3000);
                 }
             }
        };


        // Event listener for search input (Drivers tab)
        if(searchInput) {
            searchInput.addEventListener('input', (e) => {
                // When searching, clear any status filter
                renderDrivers(e.target.value, '');
            });
        }


        // Event listener for add driver button
        if(addDriverBtn) addDriverBtn.addEventListener('click', openAddModal);

        // Event listener for close add/edit driver modal button
        if(closeModalBtn) {
            closeModalBtn.addEventListener('click', () => {
                driverModal.classList.add('hidden');
                driverForm.reset(); // Reset form on close
                 currentPermitImagePreview.classList.add('hidden'); // Hide preview on close
                 currentPermitImagePreview.src = ''; // Clear preview src on close
            });
        }


        // Close add/edit driver modal when clicking outside the form
        if(driverModal) {
             driverModal.addEventListener('click', (e) => {
                if (e.target === driverModal) {
                    if(closeModalBtn) closeModalBtn.click(); // Use the close button's logic
                }
            });
        }


        // Event listener for driver form submission
        if(driverForm) driverForm.addEventListener('submit', handleDriverFormSubmit);

        // Event listener for print options button (Drivers tab)
        if(printOptionsBtn) {
            printOptionsBtn.addEventListener('click', () => {
                if(printOptionsModal) printOptionsModal.classList.remove('hidden');
            });
        }


        // Event listener for close print options modal button (Drivers tab)
        if(closePrintModalBtn) {
            closePrintModalBtn.addEventListener('click', () => {
                if(printOptionsModal) printOptionsModal.classList.add('hidden');
            });
        }


        // Close print options modal when clicking outside (Drivers tab)
        if(printOptionsModal) {
             printOptionsModal.addEventListener('click', (e) => {
                if (e.target === printOptionsModal) {
                    if(closePrintModalBtn) closePrintModalBtn.click(); // Use the close button's logic
                }
            });
        }


        // Event listener for confirming print in the options modal (Drivers tab)
        if(confirmPrintBtn) confirmPrintBtn.addEventListener('click', handlePrint);


        // Event listener for backup button (Drivers tab)
        if(backupBtn) backupBtn.addEventListener('click', backupData);

        // Event listeners for image modal (Drivers tab)
        if(closeImageModalBtn) closeImageModalBtn.addEventListener('click', closeImageModal);

        // Close image modal when clicking outside the image content (Drivers tab)
        if(imageModal) {
            imageModal.addEventListener('click', (e) => {
                if (e.target === imageModal) {
                    closeImageModal();
                }
            });
        }


        // --- Event Listeners for Driver Summary Cards ---
        if(summaryCards) {
            summaryCards.forEach(card => {
                card.addEventListener('click', () => {
                    const status = card.getAttribute('data-status');
                    if(searchInput) renderDrivers(searchInput.value, status); // Filter by status and current search term
                    showTab('drivers'); // Switch to drivers tab
                });
            });
        }


        // --- Event Listener for Show All Button (Drivers tab) ---
        if(showAllBtn) {
            showAllBtn.addEventListener('click', () => {
                if(searchInput) renderDrivers(searchInput.value, ''); // Render all drivers with current search term
            });
        }

        // --- Event Listener for Edit/Delete buttons on the driver table ---
        // Using event delegation on the table body
        if(driversTableBody) {
            driversTableBody.addEventListener('click', (e) => {
                const target = e.target;
                const editButton = target.closest('.text-indigo-600');
                const deleteButton = target.closest('.text-red-600');

                if (editButton) {
                    const row = editButton.closest('tr');
                    const driverId = parseInt(row.querySelector('td:first-child').textContent);
                    editDriver(driverId);
                } else if (deleteButton) {
                     const row = deleteButton.closest('tr');
                    const driverId = parseInt(row.querySelector('td:first-child').textContent);
                    deleteDriver(driverId);
                }
            });
        }

        // --- Event Listeners for Stations ---

        // Event listener for add station button
        if(addStationBtn) addStationBtn.addEventListener('click', openAddStationModal);

        // Event listener for close add/edit station modal button
        if(closeStationModalBtn) {
             closeStationModalBtn.addEventListener('click', () => {
                 stationModal.classList.add('hidden');
                 stationForm.reset(); // Reset form on close
             });
        }

        // Close add/edit station modal when clicking outside
        if(stationModal) {
             stationModal.addEventListener('click', (e) => {
                if (e.target === stationModal) {
                    if(closeStationModalBtn) closeStationModalBtn.click();
                }
            });
        }

        // Event listener for station form submission
        if(stationForm) stationForm.addEventListener('submit', handleStationFormSubmit);

        // Event listener for Edit/Delete buttons on the station table
        // Using event delegation on the table body
        if(stationsTableBody) {
            stationsTableBody.addEventListener('click', (e) => {
                const target = e.target;
                const editButton = target.closest('.text-indigo-600');
                const deleteButton = target.closest('.text-red-600');

                if (editButton) {
                    const row = editButton.closest('tr');
                    const stationId = parseInt(row.querySelector('td:first-child').textContent);
                    editStation(stationId);
                } else if (deleteButton) {
                     const row = deleteButton.closest('tr');
                    const stationId = parseInt(row.querySelector('td:first-child').textContent);
                    deleteStation(stationId);
                }
            });
        }

        // --- Event Listeners for Orders ---

        // Event listener for order form submission
        if(orderForm) orderForm.addEventListener('submit', handleOrderFormSubmit);

        // Event listener for inline editing on the orders table
        if(ordersTableBody) {
             ordersTableBody.addEventListener('dblclick', handleOrderTableEdit); // Use dblclick to start editing
        }

         // Event listener for delete button on the orders table
        if(ordersTableBody) {
             ordersTableBody.addEventListener('click', (e) => {
                 const target = e.target;
                 const deleteButton = target.closest('.text-red-600');

                 if (deleteButton) {
                     const row = deleteButton.closest('tr');
                     const orderId = parseInt(row.getAttribute('data-order-id'));
                     deleteOrder(orderId);
                 }
             });
        }

        // Event listener for order search input
        if(orderSearchInput) {
            orderSearchInput.addEventListener('input', (e) => {
                renderOrders(e.target.value); // Re-render orders table with search filter
            });
        }


    </script>

</body>
</html>
