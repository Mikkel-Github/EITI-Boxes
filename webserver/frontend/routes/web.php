<?php

use App\Http\Controllers\ProfileController;
use Illuminate\Foundation\Application;
use Illuminate\Support\Facades\Route;
use Inertia\Inertia;
use App\Http\Middleware\CorsMiddleware;

// Apply CORS Middleware to all routes
Route::middleware([CorsMiddleware::class])->group(function () {
    Route::get('/', function () {
        return Inertia::render('SimulationSetup');
    });

    // Uncomment and add any additional routes as needed
    /*
    Route::get('/dashboard', function () {
        return Inertia::render('Dashboard');
    })->middleware(['auth', 'verified'])->name('dashboard');

    Route::middleware('auth')->group(function () {
        Route::get('/profile', [ProfileController::class, 'edit'])->name('profile.edit');
        Route::patch('/profile', [ProfileController::class, 'update'])->name('profile.update');
        Route::delete('/profile', [ProfileController::class, 'destroy'])->name('profile.destroy');
    });
    */
});

// Include auth routes
require __DIR__ . '/auth.php';
