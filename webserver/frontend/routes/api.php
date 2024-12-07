<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\ReportController;

Route::post('/report', [ReportController::class, 'store']); // Save a new Report
Route::get('/report', [ReportController::class, 'index']); // Get all Reports
Route::patch('/report/{id}', [ReportController::class, 'update']); // Update a specific Report
